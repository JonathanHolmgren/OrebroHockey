import streamlit as st
import pandas as pd

# ---------- Logotyp ----------
st.sidebar.image("OrebroHockeyLogo.svg", width=150)

# ---------- Exempeldata med ligainformation ----------
def hämta_spelardata():
    data = [
    # NHL
    {
        "namn": "Connor McDavid",
        "mål": 26,
        "assist": 74,
        "skott": 254,
        "brytningar": 23,
        "blockeringar": 3,
        "liga": "NHL",
        "bild_url": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3895074.png&w=350&h=254"
    },
    {
        "namn": "Gustav Forsling",
        "mål": 32,
        "assist": 45,
        "skott": 120,
        "brytningar": 6,
        "blockeringar": 3,
        "liga": "NHL",
        "bild_url": "https://b.fssta.com/uploads/application/nhl/headshots/4661.vresize.350.350.medium.72.png"
    },
    {
        "namn": "Carl Grundstrom",
        "mål": 65,
        "assist": 23,
        "skott": 201,
        "brytningar": 1,
        "blockeringar": 3,
        "liga": "NHL",
        "bild_url": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4271565.png&w=350&h=254"
    },
    {
        "namn": "William Eklund",
        "mål": 23,
        "assist": 21,
        "skott": 150,
        "brytningar": 32,
        "blockeringar": 2,
        "liga": "NHL",
        "bild_url": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4874721.png"
    },

    # SHL
    {
        "namn": "Sean Malone",
        "mål": 32,
        "assist": 23,
        "skott": 170,
        "brytningar": 5,
        "blockeringar": 3,
        "liga": "SHL",
        "bild_url": "https://cdn1-photos.shl.se/photos/25/06/69869b2f-1879-4f48-8e10-583733821d2amalone.jpg?ixlib=js-3.8.0&w=689&s=92dd817a0c4ec7309c0132e205bcc678"
    },
    {
        "namn": "Egor Polin",
        "mål": 60,
        "assist": 20,
        "skott": 180,
        "brytningar": 23,
        "blockeringar": 10,
        "liga": "SHL",
        "bild_url": "https://cdn1-photos.shl.se/photos/25/04/42117260-6eaf-42c5-86c6-68dedb1af3e8polin.jpg?ixlib=js-3.8.0&w=689&s=586ced3b952623cd92b01ec70385fd2a"
    },
    {
        "namn": "Theodor Niederbach",
        "mål": 32,
        "assist": 20,
        "skott": 120,
        "brytningar": 10,
        "blockeringar": 2,
        "liga": "SHL",
        "bild_url": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQoxrLocJc7y1haP8h0aMpS8nW7eRhgvmwAFpoSZb1Wa5cx2vpECjTTcVPvYghLXjaHjDANerCa9lUupVvHamY4ig"
    },
    {
        "namn": "Wiktor Nilsson",
        "mål": 40,
        "assist": 20,
        "skott": 190,
        "brytningar": 3,
        "blockeringar": 4,
        "liga": "SHL",
        "bild_url": "https://gallerix.se/gallery/7/8/1/1/53487-800.jpg"
    },

    # Hockeyallsvenskan
    {
        "namn": "Dick Axelsson",
        "mål": 60,
        "assist": 20,
        "skott": 120,
        "brytningar": 15,
        "blockeringar": 12,
        "liga": "Hockeyallsvenskan",
        "bild_url": "https://imgk.svenskafans.com/articlemedia/image-original/43832.jpg"
    },
    {
        "namn": "Fredrik Forsberg",
        "mål": 30,
        "assist": 28,
        "skott": 120,
        "brytningar": 18,
        "blockeringar": 14,
        "liga": "Hockeyallsvenskan",
        "bild_url": "https://cdn.ramses.nu/sports/player/portrait/1000/qQ9-22516woJU-1659518308.jpg"
    },
    {
        "namn": "Andrew Vanderbeck",
        "mål": 20,
        "assist": 20,
        "skott": 120,
        "brytningar": 10,
        "blockeringar": 8,
        "liga": "Hockeyallsvenskan",
        "bild_url": "https://s8y-cdn-sp-photos.imgix.net/https%3A%2F%2Fcdn.ramses.nu%2Fsports%2Fplayer%2Fportrait%2F08d05642-55d6-4378-9656-5741ea390a85AJ%20Vanderbeck.jpg?ixlib=js-3.8.0&s=263d51e24c0326374b019109334c28ad"
    },
    {
        "namn": "Nolan Stevens",
        "mål": 30,
        "assist": 18,
        "skott": 140,
        "brytningar": 22,
        "blockeringar": 15,
        "liga": "Hockeyallsvenskan",
        "bild_url": "https://lscluster.hockeytech.com/download.php?client_code=ahl&file_path=media/d4ca69a7e27e7fba6fb02824287ab10b.png"
    }
]
    return pd.DataFrame(data)

# ---------- Kategoriformler ----------
KATEGORIER = {
    "Bästa offensiva spelare": lambda df: df["mål"] + df["assist"],
    "Mest defensiva": lambda df: df["brytningar"] + df["blockeringar"],
    "Effektivitet": lambda df: (df["mål"] / df["skott"]).fillna(0)
}

# ---------- UI-val ----------
st.title("Spelarstatistik")

val_liga = st.selectbox("Välj liga", ["NHL", "SHL", "Hockeyallsvenskan"])
val_kategori = st.selectbox("Välj kategori", list(KATEGORIER.keys()))

# ---------- Hämta och filtrera data ----------
df = hämta_spelardata()
df = df[df["liga"] == val_liga]

if df.empty:
    st.warning("Inga spelare hittades för den valda ligan.")
else:
    df["Resultat"] = KATEGORIER[val_kategori](df)
    df = df.sort_values("Resultat", ascending=False)

    # # ---------- Visa spelare ----------

st.subheader("Resultat:")

for _, row in df.iterrows():
    with st.container():
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(row["bild_url"], width=100)
        with cols[1]:
            st.markdown(f"**{row['namn']}**")
            st.write(f"Resultat: {row['Resultat']:.2f}")

            # Visa detaljer beroende på vald kategori
            if val_kategori == "Bästa offensiva spelare":
                st.write(f"Mål: {row['mål']}, Assist: {row['assist']}")
            elif val_kategori == "Mest defensiva":
                st.write(f"Brytningar: {row['brytningar']}, Blockeringar: {row['blockeringar']}")
            elif val_kategori == "Effektivitet":
                st.write(f"Mål: {row['mål']}, Skott: {row['skott']}")
