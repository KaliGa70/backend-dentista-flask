# Claves y tiempos para JWT
SECRET_KEY = 'mi_clave_secreta_para_firmar_sesiones'
JWT_SECRET_KEY = 'mi_clave_secreta_para_firmar_tokens_jwt'
JWT_ACCESS_TOKEN_EXPIRES = 3600

# JWT en cookies
JWT_TOKEN_LOCATION = ['cookies']
JWT_COOKIE_CSRF_PROTECT = True
JWT_ACCESS_COOKIE_PATH = '/'
JWT_REFRESH_COOKIE_PATH = '/auth/refresh'

# En desarrollo, Secure debe ser False para HTTP
JWT_COOKIE_SECURE = False
JWT_COOKIE_SAMESITE = 'Lax'
