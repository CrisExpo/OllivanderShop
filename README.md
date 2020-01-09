# OllivanderShop



## Tareas a realizar

### Lógica

1. Refactoriza el código de la lógica para que sea fácil de entender, barato de modificar y no cambie el comportamiento observable del código existente.
2. El código existente pasa los casos test. Asegúrate de que el tuyo también, sin modificarlos.
3. Haz un evolutivo del sistema para que sea posible añadir al inventario un nuevo tipo de item llamado "_Conjured_". Los “_Conjured_” items degradan su calidad el doble de rápido que un item normal. Añade esta lógica al sistema así como los casos test que necesites.

**WARNING**: no alteres la clase `Item` o las propiedades de `Items`  porque el colegio profesional de goblings no cree en la propiedad compartida del código y suele enviar inquisidores por la tienda de vez en cuando para chequear que se respetan su certificación de _gobbling inside_.

Aquí está el **repo donde Dobbie publicó el código**, que en realidad es el repo de Emily Bache con el kata para varios lenguajes:
https://github.com/emilybache/GildedRose-Refactoring-Kata

Las **reglas de la lógica del negocio** están "explicadas" aquí:
http://iamnotmyself.com/2011/02/14/refactor-this-the-gilded-rose-kata/ 

Aquí los **casos test**:
https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/master/texttests/ThirtyDays


### Base de datos

1. Crea una base de datos SQL que permita realizar CRUD sobre el inventario.
2. El inventario inicial es el que especifica el primer caso test, el existente en el "día 0". Recuerda realizar un esquema que permita ampliarlo con el nuevo tipo de ítem "_Conjured_":
   
```
name, sellIn, quality
+5 Dexterity Vest, 10, 20
Aged Brie, 2, 0
Elixir of the Mongoose, 5, 7
Sulfuras, Hand of Ragnaros, 0, 80
Sulfuras, Hand of Ragnaros, -1, 80
Backstage passes to a TAFKAL80ETC concert, 15, 20
Backstage passes to a TAFKAL80ETC concert, 10, 49
Backstage passes to a TAFKAL80ETC concert, 5, 49
Conjured Mana Cake, 3, 6
```

### App web

Como quieres modernizar un poco el sistema de gestión de la tienda de Ollivander, decides desarrollar una app web que permita visualizar el estado del inventario y realizar las operaciones básicas CRUD.

Esto supone tres capas en tu aplicación.

1. Capa de presentación y _frontend_.
   - Utilizando HTML y CSS construye un pequeño sitio web para la intranet, con una interfaz de usuario/a que permita a Ollivander realizar las operaciones CRUD básicas. 
2. Capa de lógica y _backend_
   - En el back encapsularás la lógica del negocio que has programado. Utilizarás un microframewwork llamado Flask para:
     - Atender y responder las peticiones que lleguen a través de un navegador web con las consulas de a la base de datos.
3. Acceso a datos (bakcend)
   - Mediante Flask, escribe el código necesario de la capa de acceso a datos, que conecte las peticiones web con la base de datos, para realizar las operaciones CRUD básicas.



