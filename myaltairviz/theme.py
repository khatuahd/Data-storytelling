import altair as alt

def my_theme():
    """
    Thème Business / Analytique pour la bibliothèque myaltairviz.
    Couleurs sobres, fond blanc, titres sérieux.
    """
    return {
        "config": {
            "background": "white",
            
            "title": {
                "fontSize": 18,
                "font": "Arial",
                "anchor": "start",
                "color": "#1f2937",  # gris foncé pour sérieux
                "fontWeight": "bold"
            },

            "axis": {
                "labelFontSize": 12,
                "titleFontSize": 14,
                "grid": True,
                "gridColor": "#e5e7eb",  # gris clair pour la grille
                "gridOpacity": 0.5,
                "domain": True,
                "ticks": True,
                "tickColor": "#1f2937"
            },

            "legend": {
                "labelFontSize": 12,
                "titleFontSize": 13
            },

            "range": {
                "category": [
                    "#1f77b4",  # bleu sérieux
                    "#ff7f0e",  # orange doux
                    "#2ca02c",  # vert discret
                    "#d62728"   # rouge pour alerte / focus
                ]
            }
        }
    }

def enable_theme():
    """
    Active le thème Business / Analytique.
    """
    alt.themes.register("my_business_theme", my_theme)
    alt.themes.enable("my_business_theme")