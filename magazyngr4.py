import streamlit as st

# --- Funkcje Logiki Magazynowej ---

def dodaj_produkt(nazwa_produktu):
    """Dodaje produkt do magazynu (listy w state sesji)."""
    if nazwa_produktu and nazwa_produktu not in st.session_state.magazyn:
        st.session_state.magazyn.append(nazwa_produktu)
        st.success(f"Dodano produkt: **{nazwa_produktu}**")
    elif nazwa_produktu in st.session_state.magazyn:
        st.warning(f"Produkt **{nazwa_produktu}** jest już w magazynie.")
    else:
        st.error("Nazwa produktu nie może być pusta.")

def usun_produkt(nazwa_produktu):
    """Usuwa produkt z magazynu."""
    if nazwa_produktu in st.session_state.magazyn:
        st.session_state.magazyn.remove(nazwa_produktu)
        st.success(f"Usunięto produkt: **{nazwa_produktu}**")
    else:
        st.warning(f"Produkt **{nazwa_produktu}** nie został znaleziony w magazynie.")

# --- Główna Aplikacja Streamlit ---

def main():
    st.title("📦 Prosta Aplikacja Magazynowa")
    st.markdown("---")

    # 1. Inicjalizacja Magazynu w Session State
    # Streamlit używa `st.session_state` do przechowywania zmiennych w trakcie sesji
    if 'magazyn' not in st.session_state:
        st.session_state.magazyn = [] # Magazyn to prosta lista nazw produktów

    st.header("➕ Dodaj Produkt")
    
    # Pole tekstowe dla nowego produktu
    nowy_produkt = st.text_input("Wpisz nazwę produktu:", key="input_dodaj")
    
    # Przycisk dodawania
    if st.button("Dodaj do Magazynu"):
        # Sprawdzamy, czy pole nie jest puste
        dodaj_produkt(nowy_produkt.strip())
        
        # Opcjonalnie: automatyczne czyszczenie pola tekstowego po dodaniu
        # Strumlit pozwala na to, ale musielibyśmy zresetować stan inputu,
        # co dla prostoty pomijamy. Wystarczy, że użytkownik kliknie ponownie w pole.
    
    st.markdown("---")

    # 2. Wyświetlanie Zawartości Magazynu
    st.header("Aktualna Zawartość Magazynu")
    
    if st.session_state.magazyn:
        # Sortowanie dla lepszej czytelności
        posortowany_magazyn = sorted(st.session_state.magazyn)
        
        # Wyświetlanie jako lista punktowana
        st.code('\n'.join(posortowany_magazyn), language='text')

        # Wersja jako tabela (opcjonalnie, można odkomentować)
        # st.dataframe({'Nazwa Produktu': posortowany_magazyn})

        st.markdown("---")
        
        # 3. Usuwanie Produktu
        st.header("➖ Usuń Produkt")
        
        # Pole wyboru (select box) z produktami do usunięcia
        produkt_do_usunięcia = st.selectbox(
            "Wybierz produkt do usunięcia:", 
            options=["-- Wybierz --"] + posortowany_magazyn,
            key="select_usun"
        )
        
        # Przycisk usuwania
        if st.button("Usuń z Magazynu") and produkt_do_usunięcia != "-- Wybierz --":
            usun_produkt(produkt_do_usunięcia)
        elif st.button("Usuń z Magazynu") and produkt_do_usunięcia == "-- Wybierz --":
            st.warning("Musisz wybrać produkt do usunięcia.")

    else:
        st.info("Magazyn jest obecnie pusty.")

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()
