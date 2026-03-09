def test_abrir_google(page):
    page.goto('https://www.google.com.br')
    page.pause()
    print(page.title())
    assert 'Google' in page.title()
    page.get_by_role("button", name="Pesquisa Google").click()

# pytest --headed --browser=firefox .\tests\test_primeiro.py
# pytest --headed --browser=chromium .\tests\test_primeiro.py
