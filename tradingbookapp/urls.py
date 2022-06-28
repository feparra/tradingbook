from django.urls import path

from . import views #se utiliza el punto por que es la ruta relativa (donde esta la carpeta)

urlpatterns = [
    path('',views.index, name='Home'),
    path('dashboard/',views.Dashboard,name="Dashboard"),
    path('notes/',views.Notes,name="Notes"),
    path('trades/',views.Trades,name="Trades"),
    path('mercados/',views.Markets,name="Mercados"),
    path('challenge/',views.Challenge,name="Challenge"),
    path('crear_trades/',views.crear_trade,name="crear_trades"),
    path('crear_notes/',views.crear_notes,name="crear_notes"),
    path('crear_mercados/',views.crear_mercados,name="crear_mercados"),
    # path('base/', views.base),
    
]
