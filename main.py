def is_prime(x):
    """
    Verifica daca x este prim
    input = x, un numar
    output = adevarat sau fals
    """
    if x < 2:
        return False
    for idx in range(2, x // 2 + 1):
        if x % idx == 0:
            return False
    else:
        return True


def get_largest_prime_below(n):
    """
    :param n: Un numar
    :return: ultimul nr umaprim mai mic decat n
    """
    ok = False
    idx = n-1
    while (not ok) and (idx > 1):
        if is_prime(idx):
            ok = True
        else:
            idx = idx - 1
    if ok:
        return idx
    else:
        return None


def test_get_largest_prime_below():
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(2) == None
    assert get_largest_prime_below(1) == None
    assert get_largest_prime_below(12) == 11


def get_age_in_days(zi, luna, an):
    """
    :return: Varsta in zile
    """
    from datetime import date
    d0 = date(an, luna, zi)
    d1 = date.today()
    delta = d1 - d0
    return(delta.days)


def test_get_age_in_days():
    assert get_age_in_days(5, 10, 2021) == 1


def is_palindrome(n) -> bool:
    """
    :param n: Un numar
    :return: True daca n e palindrom si Flase daca nu este palindrom
    """
    aux = 0
    number = n
    while number>0:
        aux = aux * 10 + number % 10
        number = number // 10
    if n == aux:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(100) == False
    assert is_palindrome(1) == True
    assert is_palindrome(11) == True


def main():
    while True:
        print(" ")
        print("1.Găsește ultimul număr prim mai mic decât un număr dat.)")
        print("2.Se dă data nașterii în formatul DD/MM/YYYY. Determinați vârsta persoanei în zile.")
        print("3.Determină dacă un număr dat este palindrom.")
        print("4. Exit")
        Optiune = int(input("Alege o optiune "))
        if Optiune == 1:
            n = int(input("Alege un numar "))
            print(get_largest_prime_below(n))
        elif Optiune == 4:
            break
        elif Optiune == 2:
            zi = int(input("Ziua: "))
            luna = int(input("Luna: "))
            an = int(input("An:"))
            print(get_age_in_days(zi, luna, an))
        else:
            n = int(input("Alege un numar "))
            print(is_palindrome(n))
if __name__ == '__main__':
    test_get_largest_prime_below()
    test_is_palindrome()
    test_get_age_in_days()

    main()
