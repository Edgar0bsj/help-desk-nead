import pytest  # noqa: F401

from module.user.user_facade import user_save


@pytest.mark.skip(
    reason="Funcionalidade em desenvolvimento, será ativada na próxima sprint."
)
def test_created():
    user_save(
        name="edgar barbosa da silva",
        cpf="12345678912",
        email="edgar@email.com",
        password="123",
        perfil="admin",
        role="admin",
    )
