from django_auth_ldap.backend import LDAPBackend

class CustomLDAPBackend(LDAPBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(f"Intentando autenticación con CustomLDAPBackend: {username}")
        return super().authenticate(request, username, password, **kwargs)

    def get_or_create_user(self, username, ldap_user):
        print("Entró en get_or_create_user")
        user, created = super().get_or_create_user(username, ldap_user)

        if created:
            print(f"Usuario nuevo creado: {username}")
            user.is_active = False
            user.save()

        return user
