def superuser_check(user):
    """
    Koristimo kod @user_passes_test dekoratora da bi dobili True ili False
    """
    return user.is_superuser
