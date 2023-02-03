
# Order Of Ecclesia API

---

## Introduction

***

A simple API made with _Django Rest Framework_ for practice purposes, based on the Castlevania: Order Of Ecclesia Glyph Union system.

The information was extracted from https://castlevania.fandom.com/wiki/Castlevania_Wiki
## Endpoints

| Route                                               	| Function                                                                                        	| Example                                         	| Method 	|
|-----------------------------------------------------	|-------------------------------------------------------------------------------------------------	|-------------------------------------------------	|--------	|
| ecclesia/weapons/                                   	| Returns a list of all Weapons/Glyphs                                                                   	| ecclesia/weapons/                               	| GET    	|
| ecclesia/weapons/_weapon_                           	| Returns data about a specific Weapon/Glyph                                                            	| ecclesia/weapons/_confodere_                      	| GET    	|
| ecclesia/glyph_union/                               	| Returns a list of all Glyph Unions                                                              	| ecclesia/glyph_union/                           	| GET    	|
| ecclesia/glyph_union/_glyph_union_                	| Returns data about a specific Glyph Union                                                       	| ecclesia/glyph_union/_union_confodere_            	| GET    	|
| ecclesia/glyph_union/?slot1=_weapon_&slot2=_weapon_	| Using the "GET" parameters slot1 and slot2, returns the corresponding Glyph Union information. Add ` ?back=dominus_agony ` for Dominus Glyph Union  	| ecclesia/glyph_union/?slot1=_lapiste_&slot2=_macir_ 	| GET    	|

---

## How to use

---

1. Create  a virtual environment and activate it:

    ` py -m virtualenv venv `

    ` .\venv\Scripts\activate.ps1  ` (Example Using windows and PowerShell)

2. Install dependencies:

    ` pip install -r requirements.txt `

3. Make migrations:

    ` py .\manage.py makemigrations`

    ` py .\manage.py migrate `

4. Run the server:
   
   `py .\manage.py runserver`

## List of Weapons

| Name            	| Alias           	|
|-----------------	|-----------------	|
| Confodere       	| confodere       	|
| Vol Confodere   	| vol_confodere   	|
| Melio Confodere 	| melio_confodere 	|
| Secare          	| secare          	|
| Vol Secare      	| vol_secare      	|
| Melio Secare    	| melio_secare    	|
| Hasta           	| hasta           	|
| Vol Hasta       	| vol_hasta       	|
| Melio Hasta     	| melio_hasta     	|
| Macir           	| macir           	|
| Vol Macir       	| vol_macir       	|
| Melio Macir     	| melio_macir     	|
| Arcus           	| arcus           	|
| Vol Arcus       	| vol_arcus       	|
| Melio Arcus     	| melio_arcus     	|
| Ascia           	| ascia           	|
| Vol Ascia       	| vol_ascia       	|
| Melio Ascia     	| melio_ascia     	|
| Falcis          	| falcis          	|
| Vol Falcis      	| vol_falcis      	|
| Melio Falcis    	| melio_falcis    	|
| Culter          	| culter          	|
| Vol Culter      	| vol_culter      	|
| Melio Culter    	| melio_culter    	|
| Scutum          	| scutum          	|
| Vol Scutum      	| vol_scutum      	|
| Melio Scutum    	| melio_scutum    	|
| Redire          	| redire          	|
| Cubus           	| cubus           	|
| Torpor          	| torpor          	|
| Lapiste         	| lapiste         	|
| Pneuma          	| pneuma          	|
| Ignis           	| ignis           	|
| Vol Ignis       	| vol_ignis       	|
| Grando          	| grando          	|
| Vol Grando      	| vol_grando      	|
| Fulgur          	| fulgur          	|
| Vol Fulgur      	| vol_fulgur      	|
| Luminatio       	| luminatio       	|
| Vol Luminatio   	| vol_luminatio   	|
| Umbra           	| umbra           	|
| Vol Umbra       	| vol_umbra       	|
| Morbus          	| morbus          	|
| Nitesco         	| nitesco         	|
| Acerbatus       	| acerbatus       	|
| Globus          	| globus          	|
| Dextro Custos   	| dextro_custos   	|
| Sinestro Custos 	| sinestro_custos 	|
| Dominus Hatred  	| dominus_hatred  	|
| Dominus Anger   	| dominus_anger   	|
| Magnes          	| magnes          	|
| Paries          	| paries          	|
| Volaticus       	| volaticus       	|
| Rapidus Fio     	| rapidus_fio     	|
| Vis Fio         	| vis_fio         	|
| Fortis Fio      	| fortis_fio      	|
| Sapiens Fio     	| sapiens_fio     	|
| Fides Fio       	| fides_fio       	|
| Felicem Fio     	| felicem_fio     	|
| Inire Pecunia   	| inire_pecunia   	|
| Arma Felix      	| arma_felix      	|
| Arma Chiroptera 	| arma_chiroptera 	|
| Arma Machina    	| arma_machina    	|
| Refectio        	| refectio        	|
| Arma Custos     	| arma_custos     	|
| Fidelis Caries  	| fidelis_caries  	|
| Fidelis Alate   	| fidelis_alate   	|
| Fidelis Polkir  	| fidelis_polkir  	|
| Fidelis Noctua  	| fidelis_noctua  	|
| Fidelis Medusa  	| fidelis_medusa  	|
| Fidelis Aranea  	| fidelis_aranea  	|
| Fidelis Mortus  	| fidelis_mortus  	|
| Dominus Agony   	| dominus_agony   	|


## List of Glyph Unions

| Name            	| Alias           	|
|-----------------	|-----------------	|
| Pulsus          	| pulsus          	|
| Union Confodere 	| union_confodere 	|
| Union Secare    	| union_secare    	|
| Union Macir     	| union_macir     	|
| Union Falcis    	| union_falcis    	|
| Union Ascia     	| union_ascia     	|
| Union Hasta     	| union_hasta     	|
| Union Culter    	| union_culter    	|
| Union Arcus     	| union_arcus     	|
| Mars            	| mars            	|
| Mercurius       	| mercurius       	|
| Iuppiter        	| iuppiter        	|
| Tellus          	| tellus          	|
| Saturnus        	| saturnus        	|
| Pluto           	| pluto           	|
| Uranus          	| uranus          	|
| Venus           	| venus           	|
| Evanescere      	| evanescere      	|
| Universitas     	| universitas     	|
| Union Lapiste   	| union_lapiste   	|
| Union Pneuma    	| union_pneuma    	|
| Union Nitesco   	| union_nitesco   	|
| Union Scutum    	| union_scutum    	|
| Union Ignis     	| union_ignis     	|
| Union Grando    	| union_grando    	|
| Union Fulgur    	| union_fulgur    	|
| Union Luminatio 	| union_luminatio 	|
| Union Umbra     	| union_umbra     	|
| Dominus         	| dominus         	|
