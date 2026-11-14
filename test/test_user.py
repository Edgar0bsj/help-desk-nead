import pytest  # noqa: F401

from module.user.user_facade import user_save


def test_created():
    user_save(
        name="edgar barbosa da silva",
        cpf="12345678912",
        email="edgar@email.com",
        password="admin123",
        perfil="admin",
        role="admin",
    )
