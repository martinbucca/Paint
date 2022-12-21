from png import escribir
import string
import gamelib          # blanco , negro   , rojo,  verde,   azul,   celeste, amarillo, rosa
COLORES_PRINCIPALES = ('#ffffff', '#000000', '#ff0000', '#00ff00', '#0000ff', '#00ffff', '#ffff00', '#ff00ff')
ANCHO_VENTANA = 500
ALTO_VENTANA = 600
ANCHO_IMAGEN_INCIAL = 12
ALTO_IMAGEN_INCIAL = 12
COLOR_FONDO = '#898685'
COLOR_TITULO = '#CFC4C0'
ANCHO_PIXEL_CENTRADO = (240, 260) #el ancho de un pixel de tamaño 20 en el centro.
ALTO_PIXEL_CENTRADO = (290, 310) #el alto de un pixel de tamaño 20 en el centro.
POSICION_PIXEL = 20
POSICION_RESPECTO_TAMAÑO = 10
TAMAÑO_IMAGEN_PNG = 50
ALTO_COLORES = (40, 70)
ANCHO_COLOR = (25, 60)
POSICION_COLOR  = 40
INGRESO_DE_COLORES = (350, 40, 460, 70)
TEXTO_INGRESO_DE_COLORES = (405, 55)
OVALO_MOSTRAR_COLOR = (465, 40, 495, 70)
LETRA_ELEGIR_OTRO_COLOR = 9
CARGAR_PPM = (40, 516, 150, 546)
GUARDAR_PPM = (200, 516, 325, 546)
GUARDAR_PNG = (360, 516, 470, 546)
TEXTO_CARGAR_PPM = (95, 531)
TEXTO_GUARDAR_PPM = (255, 531)
TEXTO_GUARDAR_PNG = (415, 531)
ALTO_FONDO_TITULO = 30
ANCHO_TEXTO_TITULO = 250
ALTO_TEXTO_TITULO = 15
UNDO = (155, 565, 245, 595)
REDO = (255, 565, 345, 595)
TEXTO_REDO = (300, 580)
TEXTO_UNDO = (200, 580)
BALDE = (390, 565, 420, 595)
MANIJA_BALDE = (390, 550, 420, 570)

# Implementacion de Pila()
class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
class Pila:
    def __init__(self):
        self.tope = None
    def apilar(self, dato):
        nodo = _Nodo(dato, self.tope)
        self.tope = nodo
    def desapilar(self):      
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato
    def ver_tope(self):          
        return self.tope.dato
    def esta_vacia(self):
        return self.tope is None


def paint_nuevo(ancho, alto):
    '''inicializa el estado del programa con una imagen vacía de ancho x alto pixels'''
    imagen_vacia = {'encabezado': 'Imagen vacia','ancho': ancho, 'alto': alto, 'intensidad': 255,'color seleccionado' : '','color ingresado': '#ffffef' ,'balde':False ,'pixeles': {}}
    for j in range (alto):
        for i in range(ancho):
            imagen_vacia['pixeles'][f'{j},{i}'] = {}
            x1 = ANCHO_PIXEL_CENTRADO[0] - POSICION_RESPECTO_TAMAÑO * ancho  + POSICION_PIXEL * i
            y1 = ALTO_PIXEL_CENTRADO[0] - POSICION_RESPECTO_TAMAÑO * alto + POSICION_PIXEL * j
            x2 = ANCHO_PIXEL_CENTRADO[1] - POSICION_RESPECTO_TAMAÑO * ancho + POSICION_PIXEL * i
            y2 = ALTO_PIXEL_CENTRADO[1] - POSICION_RESPECTO_TAMAÑO * alto + POSICION_PIXEL * j
            imagen_vacia['pixeles'][f'{j},{i}']['pos'] = (x1, y1, x2, y2)
            imagen_vacia['pixeles'][f'{j},{i}']['color'] = '#' + f'{255:02x}' * 3
    return imagen_vacia

def mostrar_balde(paint):
    '''Muestra el balde en su posicion y con su respectivo diseño en la interfaz del paint'''
    gamelib.draw_oval(MANIJA_BALDE[0], MANIJA_BALDE[1], MANIJA_BALDE[2], MANIJA_BALDE[3],fill=COLOR_FONDO, width=3)
    if paint['balde']: #si el balde esta seleccionado se, rellena con el color a pintar
            gamelib.draw_rectangle(BALDE[0], BALDE[1], BALDE[2], BALDE[3],fill=paint['color seleccionado'],outline='white',width=4)
    else:
        gamelib.draw_rectangle(BALDE[0], BALDE[1], BALDE[2], BALDE[3],width=1)
def mostar_undo_redo(paint):
    '''Muestra los botones de 'UNDO' y 'REDO' en sus respectivas posiciones del paint'''
    gamelib.draw_rectangle(UNDO[0], UNDO[1], UNDO[2], UNDO[3], activeoutline='green')
    gamelib.draw_rectangle(REDO[0], REDO[1], REDO[2], REDO[3], activeoutline='green')
    gamelib.draw_text('UNDO', TEXTO_UNDO[0], TEXTO_UNDO[1], fill='black', bold=True, activefill='green')
    gamelib.draw_text('REDO',TEXTO_REDO[0], TEXTO_REDO[1], fill='black', bold=True, activefill='green')

def mostar_pixeles(paint):
    '''Muestra los pixeles a dibujar en la interfaz, centrados.'''
    for pixel in paint['pixeles']:
        x1, y1, x2, y2 = paint['pixeles'][pixel]['pos'][0], paint['pixeles'][pixel]['pos'][1], paint['pixeles'][pixel]['pos'][2], paint['pixeles'][pixel]['pos'][3]
        color = paint['pixeles'][pixel]['color']
        gamelib.draw_rectangle(x1, y1, x2, y2, fill= color)

def mostrar_guardar_cargar(paint):
    '''Muestra los botenes para cargar/guardar imagenes en sus posiciones respectivas del paint'''
    gamelib.draw_rectangle(CARGAR_PPM[0], CARGAR_PPM[1], CARGAR_PPM[2], CARGAR_PPM[3], fill='white', activeoutline='green')
    gamelib.draw_rectangle(GUARDAR_PPM[0], GUARDAR_PPM[1], GUARDAR_PPM[2], GUARDAR_PPM[3], fill='white', activeoutline='green')
    gamelib.draw_rectangle(GUARDAR_PNG[0], GUARDAR_PNG[1], GUARDAR_PNG[2], GUARDAR_PNG[3], fill='white', activeoutline='green')
    gamelib.draw_text('Upload PPM',TEXTO_CARGAR_PPM[0], TEXTO_CARGAR_PPM[1], fill='black', activefill='green',bold=True)
    gamelib.draw_text('Save as PPM',TEXTO_GUARDAR_PPM[0], TEXTO_GUARDAR_PPM[1],fill='black', activefill='green',bold=True)
    gamelib.draw_text('Save as PNG',TEXTO_GUARDAR_PNG[0], TEXTO_GUARDAR_PNG[1],fill='black', activefill='green',bold=True)

def paint_mostrar(paint):
    '''dibuja la interfaz de la aplicación en la ventana. Muestra todos los elementos
    en sus respectivas posiciones y con sus respectivos diseños, con los que el usuario puede interactuar'''
    gamelib.draw_begin()
    
    # fondo y titulo.
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ALTO_VENTANA, fill= COLOR_FONDO)
    gamelib.draw_rectangle(0, 0, ANCHO_VENTANA, ALTO_FONDO_TITULO, fill= COLOR_TITULO)
    gamelib.draw_text('AlgoPaint', ANCHO_TEXTO_TITULO, ALTO_TEXTO_TITULO, bold=True, fill = 'black')
    
    #dibujar pixeles
    mostar_pixeles(paint)   
    # dibujar colores de atajo
    for i in range(len(COLORES_PRINCIPALES)):   
        if COLORES_PRINCIPALES[i] == paint['color seleccionado']:
            gamelib.draw_rectangle(POSICION_COLOR * i + ANCHO_COLOR[0], ALTO_COLORES[0], POSICION_COLOR * i + ANCHO_COLOR[1], ALTO_COLORES[1] , fill = COLORES_PRINCIPALES[i], outline='white', width=4 )
        else:
            gamelib.draw_rectangle(POSICION_COLOR * i + ANCHO_COLOR[0], ALTO_COLORES[0], POSICION_COLOR * i + ANCHO_COLOR[1], ALTO_COLORES[1] , fill = COLORES_PRINCIPALES[i], activeoutline='white' )
    #dibujar ingreso de colores
    gamelib.draw_rectangle(INGRESO_DE_COLORES[0], INGRESO_DE_COLORES[1], INGRESO_DE_COLORES[2], INGRESO_DE_COLORES[3], fill= '#ffffef', activeoutline='green')
    gamelib.draw_text('Pick another color', TEXTO_INGRESO_DE_COLORES[0], TEXTO_INGRESO_DE_COLORES[1], fill='black', bold=True, activefill='green', size = LETRA_ELEGIR_OTRO_COLOR)
    if paint['color ingresado'] == paint['color seleccionado']:       
        gamelib.draw_oval(OVALO_MOSTRAR_COLOR[0], OVALO_MOSTRAR_COLOR[1], OVALO_MOSTRAR_COLOR[2], OVALO_MOSTRAR_COLOR[3],fill= paint['color seleccionado'], outline = 'white', width=4)
    mostrar_guardar_cargar(paint)
    mostrar_balde(paint)
    mostar_undo_redo(paint)
    gamelib.draw_end()
    
# funciones de cargar/gurdar imagenes.

def guardar_ppm(paint):
    '''Guarda una imagen en formato ppm.'''
    nombre = gamelib.input('Save as:')
    if nombre == None: #si apreta la cruz
        return
    paint['encabezado'] = nombre
    with open(nombre, 'w') as ppm:
        ppm.write(paint['encabezado'] + '\n')
        ppm.write(str(paint['ancho']) + ' ' + str(paint['alto']) + '\n')
        ppm.write(str(paint['intensidad']) + '\n')
        for pixel in paint['pixeles']:
            r, g, b = int(paint['pixeles'][pixel]['color'][1:3], 16), int(paint['pixeles'][pixel]['color'][3:5], 16), int(paint['pixeles'][pixel]['color'][5:7], 16)             
            ppm.write(str(r) + ' ')
            ppm.write(str(g) + ' ')
            ppm.write(str(b) + '   ')
            if int(pixel.split(',')[1]) + 1 == paint['ancho']: #es el ultimo de la fila
                ppm.write('\n') #para que se guarde en forma de matriz
    
def cargar_ppm(paint):
    '''Abre una imagen dada en formato ppm en la interfaz'''
    nombre = gamelib.input('Open PPM:')
    if nombre == None: #apreta la cruz
        return
    try:
        ppm = open(nombre)
        archivo = []
        for linea in ppm:
            archivo += linea.rstrip().split() #todo lo que esta en el archivo lo meto en la lista archivo
        paint['encabezado'] = archivo[0]
        paint['ancho'], paint['alto'] = int(archivo[1]), int(archivo[2])
        paint['intensidad'] = int(archivo[3])
        paint['pixeles'] = {}
        for j in range(paint['alto']):
            for i in range(paint['ancho']):
                paint['pixeles'][f'{j},{i}'] = {} #actualizo la cantidad de pixeles a lo que dice la imagen cargada
        colores = archivo[4::] #lista de rgb de todos los colores del archivo
        c = 0 
        for j in range(paint['alto']):
            for i in range(0, len(colores)//paint['alto'], 3):
                x1 = ANCHO_PIXEL_CENTRADO[0] - POSICION_RESPECTO_TAMAÑO * paint['ancho']  + POSICION_PIXEL * i//3
                y1 = ALTO_PIXEL_CENTRADO[0] - POSICION_RESPECTO_TAMAÑO * paint['alto'] + POSICION_PIXEL * j
                x2 = ANCHO_PIXEL_CENTRADO[1] - POSICION_RESPECTO_TAMAÑO * paint['ancho'] + POSICION_PIXEL * i//3
                y2 = ALTO_PIXEL_CENTRADO[1] - POSICION_RESPECTO_TAMAÑO * paint['alto'] + POSICION_PIXEL * j
                paint['pixeles'][f'{j},{i//3}']['pos'] = (x1, y1, x2, y2)
                r, g, b = int(colores[c]), int(colores[c + 1]), int(colores[c + 2])
                paint['pixeles'][f'{j},{i//3}']['color'] = '#' + f'{r:02x}' + f'{g:02x}' + f'{b:02x}'
                c += 3
        ppm.close()
    except (FileNotFoundError, IOError, EOFError,PermissionError, UnicodeDecodeError):
        gamelib.say(f'Error. The file {nombre} does not exist or can not be opened.')
    except ValueError:
        gamelib.say('Sorry. Something went wrong')

def guardar_png(paint):
    '''Guarda una imagen en formato png'''
    nombre = gamelib.input('Save as:')
    if nombre == None:
        return
    paleta = []
    imagen = []
    for pixel in paint['pixeles']:
        r, g, b = int(paint['pixeles'][pixel]['color'][1:3], 16), int(paint['pixeles'][pixel]['color'][3:5], 16), int(paint['pixeles'][pixel]['color'][5:7], 16)
        color =  (r, g, b)
        if color not in paleta:
            paleta.append(color)
    for j in range(paint['alto']):
        imagen.append([])
        for i in range(paint['ancho']):
            r, g, b = int(paint['pixeles'][f'{j},{i}']['color'][1:3], 16), int(paint['pixeles'][f'{j},{i}']['color'][3:5], 16), int(paint['pixeles'][f'{j},{i}']['color'][5:7], 16)
            for color in paleta:
                if (r, g, b) == color:
                    imagen[j] += [paleta.index(color)] * TAMAÑO_IMAGEN_PNG 
    imagen_final = []
    for i in range(len(imagen)):
        imagen_final += [imagen[i]] * TAMAÑO_IMAGEN_PNG  
    escribir(nombre, paleta, imagen_final) 



def validar_color(color):
    '''Dada una cadena de texto, valida que sea un color hexadecimal.'''
    for c in color[1:]:
        if c not in string.hexdigits:
            return False
    return True



def pintar_alrededor(pixel, paint, color_a): #pixel = j,i
    if int(pixel.split(',')[0]) < 0 or int(pixel.split(',')[0]) == paint['alto'] or int(pixel.split(',')[1]) < 0 or int(pixel.split(',')[1]) == paint['ancho']:
        return
    if paint['pixeles'][pixel]['color'] != color_a:
        return
    
    else:
        if paint['pixeles'][pixel]['color'] == color_a:
            paint['pixeles'][pixel]['color'] = paint['color seleccionado']
        pintar_alrededor(f'{int(pixel.split(",")[0]) + 1},{int(pixel.split(",")[1])}', paint, color_a) #el de abajo
        pintar_alrededor(f'{int(pixel.split(",")[0]) - 1},{int(pixel.split(",")[1])}', paint, color_a) #el de arriba 
        pintar_alrededor(f'{int(pixel.split(",")[0])},{int(pixel.split(",")[1]) + 1}', paint, color_a) #el de la derecha
        pintar_alrededor(f'{int(pixel.split(",")[0])},{int(pixel.split(",")[1]) - 1}', paint, color_a) #el de la izquierda
            

def main():
    
    gamelib.title("AlgoPaint")
    gamelib.resize(ANCHO_VENTANA, ALTO_VENTANA)
    paint = paint_nuevo(ANCHO_IMAGEN_INCIAL, ALTO_IMAGEN_INCIAL)
    acciones_hechas = Pila()
    acciones_deshechas = Pila()
    while gamelib.is_alive():
        
        paint_mostrar(paint)

        ev = gamelib.wait()
        if not ev:
            break
        
        
        if ev.type == gamelib.EventType.ButtonPress and ev.mouse_button == 1: 
            x, y = ev.x, ev.y   
                
            for i in range(len(COLORES_PRINCIPALES)):
                
                if POSICION_COLOR * i + ANCHO_COLOR[0] <= x <= POSICION_COLOR * i + ANCHO_COLOR[1] and ALTO_COLORES[0] <= y <= ALTO_COLORES[1]:
                    acciones_deshechas = Pila() #si se toca un color, se pierde la posibilidad de hacer redo hasta que se haga undo
                    paint['color seleccionado'] = COLORES_PRINCIPALES[i]
                    paint['balde'] = False # si el balde esta activado y se toca un color despues, lo desactiva
                    
                

            for pixel in paint['pixeles']:
                
                x1, y1, x2, y2 = paint['pixeles'][pixel]['pos'][0], paint['pixeles'][pixel]['pos'][1], paint['pixeles'][pixel]['pos'][2], paint['pixeles'][pixel]['pos'][3]
                if x1 < x < x2 and y1 < y < y2 and paint['color seleccionado'] != '':
                    if paint['balde']:
                        color_a = paint['pixeles'][pixel]['color']
                        pintar_alrededor(pixel, paint, color_a )
                    else:
                        
                        pos_pixel = paint['pixeles'][pixel]['pos']
                        color_anterior = paint['pixeles'][pixel]['color']
                        paint['pixeles'][pixel]['color'] = paint['color seleccionado'] #se pinta el pixel del color seleccionado si es que se selecciono alguno.
                        color_posterior = paint['pixeles'][pixel]['color']
                        acciones_hechas.apilar((pos_pixel, color_anterior, color_posterior))#apilo la posicion del pixel el color antes de ser pintado y despues

            if INGRESO_DE_COLORES[0] <= x <= INGRESO_DE_COLORES[2] and INGRESO_DE_COLORES[1] <= y <= INGRESO_DE_COLORES[3]:
                acciones_deshechas = Pila()
                color = gamelib.input('Enter a color in hexadecimal code (#RRGGBB)')
                if color == None:
                    continue
                if validar_color(color) == False:
                    gamelib.say('Invalid color, you should enter something like this: #00ff23')
                else:
                    paint['color ingresado'] = color
                    paint['color seleccionado'] = color
                    paint['balde'] = False
                    

            if GUARDAR_PPM[0] < x <  GUARDAR_PPM[2] and GUARDAR_PPM[1] < y < GUARDAR_PPM[3]:
                acciones_deshechas = Pila()
                guardar_ppm(paint)

            if CARGAR_PPM[0] < x <  CARGAR_PPM[2] and CARGAR_PPM[1] < y < CARGAR_PPM[3]:
                acciones_deshechas = Pila()
                cargar_ppm(paint)

            if GUARDAR_PNG[0] < x <  GUARDAR_PNG[2] and GUARDAR_PNG[1] < y < GUARDAR_PNG[3]:
                acciones_deshechas = Pila()
                guardar_png(paint)

            if UNDO[0] < x < UNDO[2] and UNDO[1] < y < UNDO[3]:
                if not acciones_hechas.esta_vacia(): #si esta vacia no hay acciones que deshacer
                    for pixel in paint['pixeles']:
                        if paint['pixeles'][pixel]['pos'] == acciones_hechas.ver_tope()[0]: 
                            paint['pixeles'][pixel]['color'] = acciones_hechas.ver_tope()[1] #le cambio el color al ultimo estado de ese color que es el tope
                            acciones_deshechas.apilar(acciones_hechas.desapilar())
                            
                            break
            if REDO[0] < x < REDO[2] and REDO[1] < y < REDO[3]:
                if not acciones_deshechas.esta_vacia(): #si esta vacia no hay acciones que rehacer
                    for pixel in paint['pixeles']:
                        if paint['pixeles'][pixel]['pos'] == acciones_deshechas.ver_tope()[0]: 
                            paint['pixeles'][pixel]['color'] = acciones_deshechas.ver_tope()[2] #le cambio el color al ultimo estado de ese color que es el tope
                            acciones_hechas.apilar(acciones_deshechas.desapilar())
                            break
            if BALDE[0] < x < BALDE[2] and BALDE[1] < y < BALDE[3]:
                acciones_deshechas = Pila()
                if paint['color seleccionado'] != '':
                    paint['balde'] = True #PARA ACTIVAR EL BALDE PRIMERO TENES QUE TENER UN COLOR SELECCIONADO
                          
gamelib.init(main)




