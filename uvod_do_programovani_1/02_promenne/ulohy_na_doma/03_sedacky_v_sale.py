# Zadani: https://kodim.cz/czechitas/uvod-do-progr-1/prvni-krucky/promenne/ulohy/sedacky-v-sale

pocet_sedacek = 350
delka_rady = 32

pocet_uplnych_rad = pocet_sedacek // delka_rady
print("Pocet uplnych rad")
print(pocet_uplnych_rad)

sedacky_v_neuplny_rade = pocet_sedacek % delka_rady
print("Pocet sedacek v neuplny rade")
print(sedacky_v_neuplny_rade)

print("Pocet sedacek, ktere musime prikoupit")
print(delka_rady - sedacky_v_neuplny_rade)

print("Pocet uplnych rad po dokoupeni sedacek")
print(pocet_uplnych_rad + 1)
