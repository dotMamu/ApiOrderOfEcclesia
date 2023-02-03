
# Order Of Ecclesia API

## Introduction

A simple API made for practice purposes, based on the Castlevania: Order Of Ecclesia Glyph Union system.


## Endpoints

| Route                                               	| Function                                                                                        	| Example                                         	| Method 	|
|-----------------------------------------------------	|-------------------------------------------------------------------------------------------------	|-------------------------------------------------	|--------	|
| ecclesia/weapons/                                   	| Returns a list of all Weapons/Glyphs                                                                   	| ecclesia/weapons/                               	| GET    	|
| ecclesia/weapons/_weapon_                           	| Returns data about a specific Weapon/Glyph                                                            	| ecclesia/weapons/_confodere_                      	| GET    	|
| ecclesia/glyph_union/                               	| Returns a list of all Glyph Unions                                                              	| ecclesia/glyph_union/                           	| GET    	|
| ecclesia/glyph_union/_glyph_union_                	| Returns data about a specific Glyph Union                                                       	| ecclesia/glyph_union/_union_confodere_            	| GET    	|
| ecclesia/glyph_union/?slot1=_weapon_&slot2=_weapon_ 	| Using the "GET" parameters slot1 and slot2, returns the corresponding Glyph Union information.  	| ecclesia/glyph_union/?slot1=_lapiste_&slot2=_macir_ 	| GET    	|


## How to run

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

