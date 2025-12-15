def maganhangzot_torol(szoveg: str) -> str:
    maganhangzok = 'aeiouAEIOU'
    return ''.join(karakter for karakter in szoveg if karakter not in maganhangzok)


if __name__ == "__main__":
    bemenet = input("Kérem, adja meg a szöveget: ")
    
    eredmeny = maganhangzot_torol(bemenet)
    
    print("\nMagánhangzók nélküli szöveg:")
    print(eredmeny)