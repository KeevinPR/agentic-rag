"""
Módulo de autenticación temporal para demos
Implementa autenticación segura con protecciones básicas
"""

import hashlib
import secrets
import logging
from datetime import datetime, timedelta
from typing import Optional, Dict
from config import DEMO_CONFIG

logger = logging.getLogger(__name__)

class DemoAuthManager:
    def __init__(self):
        self.active_sessions = {}
        self.failed_attempts = {}
        
    def _hash_password(self, password: str, salt: str = None) -> tuple:
        """Hash password con salt para seguridad básica"""
        if not salt:
            salt = secrets.token_hex(16)
        
        pwd_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000  # iterations
        )
        return pwd_hash.hex(), salt
    
    def _check_rate_limit(self, identifier: str) -> bool:
        """Prevenir ataques de fuerza bruta"""
        now = datetime.now()
        attempts = self.failed_attempts.get(identifier, [])
        
        # Limpiar intentos antiguos (últimos 15 minutos)
        recent_attempts = [
            attempt for attempt in attempts 
            if now - attempt < timedelta(minutes=15)
        ]
        
        self.failed_attempts[identifier] = recent_attempts
        return len(recent_attempts) < 5  # Máximo 5 intentos
    
    def authenticate(self, username: str, password: str, client_ip: str = None) -> Optional[Dict]:
        """Autenticar usuario demo con protecciones básicas"""
        
        # Verificar si las demos están habilitadas
        if not DEMO_CONFIG["enabled"]:
            logger.warning("Demo mode is disabled")
            return None
            
        # Verificar fecha de expiración
        try:
            expire_date = datetime.strptime(DEMO_CONFIG["expires_at"], "%Y-%m-%d")
            if datetime.now() > expire_date:
                logger.warning("Demo has expired")
                return None
        except ValueError:
            logger.error("Invalid expiration date format")
            return None
        
        # Rate limiting por IP
        rate_key = client_ip or "unknown"
        if not self._check_rate_limit(rate_key):
            logger.warning(f"Rate limit exceeded for {rate_key}")
            return None
            
        # Verificar credenciales
        user_config = DEMO_CONFIG["credentials"].get(username)
        if not user_config or user_config["password"] != password:
            # Registrar intento fallido
            now = datetime.now()
            if rate_key not in self.failed_attempts:
                self.failed_attempts[rate_key] = []
            self.failed_attempts[rate_key].append(now)
            logger.warning(f"Failed login attempt: {username} from {rate_key}")
            return None
        
        # Crear sesión
        session_id = secrets.token_urlsafe(32)
        session_data = {
            "user_id": username,
            "session_id": session_id,
            "role": user_config["role"],
            "permissions": user_config["permissions"],
            "rate_limit": user_config["rate_limit"],
            "created_at": datetime.now(),
            "expires_at": datetime.now() + timedelta(seconds=user_config["session_timeout"]),
            "client_ip": client_ip
        }
        
        self.active_sessions[session_id] = session_data
        logger.info(f"User authenticated successfully: {username}")
        return session_data
    
    def validate_session(self, session_id: str) -> Optional[Dict]:
        """Validar sesión activa"""
        session = self.active_sessions.get(session_id)
        if not session:
            return None
            
        # Verificar expiración
        if datetime.now() > session["expires_at"]:
            del self.active_sessions[session_id]
            logger.info(f"Session expired for user: {session.get('user_id')}")
            return None
            
        return session
    
    def logout(self, session_id: str):
        """Cerrar sesión"""
        if session_id in self.active_sessions:
            user_id = self.active_sessions[session_id].get('user_id')
            del self.active_sessions[session_id]
            logger.info(f"User logged out: {user_id}")
    
    def get_active_sessions_count(self) -> int:
        """Obtener número de sesiones activas"""
        return len(self.active_sessions)

# Instancia global
demo_auth = DemoAuthManager()
