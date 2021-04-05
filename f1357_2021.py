from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from f1357 import Ui_MainWindow  # importing our generated file

import sys


lista_empleado=[] 
lista_renumeraciones=[] 
lista_deducciones=[] 
lista_deducciones_art23=[] 
lista_calculo=[]
lista_txt_1357=[]
cabecera1=""
nombrearchivoguardado=""




class cabecera:
    def __init__(self,tiporegistro,cuitagente,periodoinformado,secuencia,codigoimpuesto,codigoconcepto,numeroformulario,
                 tipo,version):
        self.tiporegistro=tiporegistro
        self.cuitagente=cuitagente
        self.periodoinformado=periodoinformado
        self.secuencia=secuencia
        self.codigoimpuesto=codigoimpuesto
        self.numeroformulario=numeroformulario
        self.tipo=tipo
        self.version=version
        
        
        
        


class trabajador:

    def __init__(self,tiporegistro,cuil,desde,hasta,meses,beneficio,largadistancia,ley27424,ley27549):
        self.tiporegistro=tiporegistro
        self.cuil=cuil
        self.desde=desde
        self.hasta=hasta
        self.meses=meses
        self.beneficio=beneficio
        self.largadistancia=largadistancia
        self.ley27424=ley27424
        self.ley27549=ley27549  
        
    def __repr__(self):
        return str(self.__dict__)
     
class renumeraciones:
    
    def __init__(self,tiporegistro,cuil,bruto,nohabitualesgrava,sac1grav,sac2grav,hextgrav,viaticosgrav,docentegrav,exentasinhoras,exentahoras,viaticosexenta,
                 docenteexenta,otrosempleosbrutgrav,otrosemplnohabigrav,otrosemplsac1grav,otrosemplsac2grav,otrosemplhsextgrav,otrosempviaticosgrav,otrosempdocgrav,
                 otrosemplexcsinhoras,otrosexenthorasextra,otrosviaticosexe,otrosdocenexe,remgravada,remnogravada,totalremu,nohabitexe,sac1exent,sec2exent,
                 ajustesgrav,ajustesnoalcanzado,otrosajustesgrav,otrosajustesnoalcanzado,otrosnohabitualesexento,otrossacexe,otrossac2exe,otrosajusgrav,otrosajusexe,ley27549,
                 otrosley27549):
        
        self.tiporegistro=tiporegistro
        self.cuil=cuil
        self.brutogravado=bruto
        self.nohabitualesgravado=nohabitualesgrava
        self.sac1cuotagravado=sac1grav
        self.sac2cuotagravado=sac2grav
        self.horasextrasgravado=hextgrav
        self.viaticosgravado=viaticosgrav
        self.docentegravado=docentegrav
        self.remuneracionnoalcanzasinhorasextras=exentasinhoras
        self.remuneracionexcentahorasextras=exentahoras
        self.viaticosexenta=viaticosexenta
        self.docenteexento=docenteexenta
        self.otrosempleos_brutogravado=otrosempleosbrutgrav
        self.otrosempleos_nohabitualesgravado=otrosemplnohabigrav
        self.otrosempleos_sac1gravado=otrosemplsac1grav
        self.otrosempleos_sac2gravado=otrosemplsac2grav
        self.otrosempleos_horasextrasgravado=otrosemplhsextgrav
        self.otrosempleos_viatiosgravado=otrosempviaticosgrav
        self.otrosempleos_docentegravado=otrosempdocgrav
        self.otrosempleos_noalcanzadosinhoras=otrosemplexcsinhoras
        self.otrosempleos_exento_horasextras=otrosexenthorasextra
        self.otrosempleos_viaticosexento=otrosviaticosexe
        self.otrosempleos_docenteexento=otrosdocenexe
        self.remuneracion_gravada=remgravada
        self.remuneracion_no_Gravada=remnogravada
        self.total_remuneracion=totalremu
        self.nohabitales_exenta=nohabitexe
        self.sac1cuotaexento=sac1exent
        self.sac2cuotaexento=sec2exent
        self.ajustes_gravado=ajustesgrav
        self.ajustes_exento=ajustesnoalcanzado
        self.otrosempleos_nohabitualesexento=otrosnohabitualesexento
        self.otrosempleos_sac1exento=otrossacexe
        self.otrosempleos_sac2exento=otrossac2exe
        self.otrosempleos_ajustesgravado=otrosajusgrav
        self.otrosempleos_ajustesnogravado=otrosajusexe
        self.ley27549=ley27549
        self.otrosempleos_ley27549=otrosley27549
    def __repr__(self):
        return str(self.__dict__)

class deducciones:
    
    def __init__(self,tiporegistro,cuil,jubilacion,otrosjub,obrasocial,otrosobrasoc,sindicato,otrossindicato,cuotamedico,primasseguromuerte,
                 seguromixta,retiroprivado,adquisicion_cuotaparte,sepelio,amortizaciones,donaciones,descxley,honorariosasisten,interesescred,apcapsoc,
                 otras_cajas,alquileres,domestico,viaticosxempleador,indumentaria,otrasdedu,totaldedugral,otras_aportjub,otras_cajasprov,
                 otras_actores,otras_fondos):
        self.tiporegistro=tiporegistro
        self.cuil=cuil      
        self.jubilacion=jubilacion
        self.otrosjub=otrosjub
        self.obrasocial=obrasocial
        self.otrosobrasoc=otrosobrasoc
        self.sindicato=sindicato
        self.otrossindicato=otrossindicato
        self.cuotamedico=cuotamedico
        self.seguromuerte=primasseguromuerte
        self.seguromixta=seguromixta
        self.retiroprivado=retiroprivado
        self.adquisicion_cuotaparte=adquisicion_cuotaparte
        self.sepelio=sepelio
        self.amortizaciones=amortizaciones
        self.donaciones=donaciones
        self.descxley=descxley
        self.honorariosasisten=honorariosasisten
        self.interesescred=interesescred
        self.apcapsoc=apcapsoc
        self.otras_cajas=otras_cajas
        self.alquileres=alquileres
        self.domestico=domestico
        self.viaticosxempleador=viaticosxempleador
        self.indumentaria=indumentaria
        self.otrasdedu=otrasdedu
        self.totaldedugral=totaldedugral
        self.otras_aportjub=otras_aportjub
        self.otras_cajasprov=otras_cajasprov
        self.otras_actores=otras_actores
        self.otras_fondos=otras_fondos
    def __repr__(self):
        return str(self.__dict__)
        
class deducciones_art_23:
    
    def __init__(self,tiporegistro,cuil,gni,deduccion_especial,deduccion_especifica,conyugue,cant_hijos,hijos,total_cargas,ded_art30,rem_suj_antes,
                 deduinca,deduincb,remsujaimp):
        self.tiporegistro=tiporegistro
        self.cuil=cuil
        self.gni=gni
        self.deduccion_especial=deduccion_especial
        self.deduccion_especifica=deduccion_especifica
        self.conyugue=conyugue
        self.cant_hijos=cant_hijos
        self.hijos=hijos
        self.total_cargas=total_cargas
        self.ded_art30=ded_art30
        self.rem_suj_antes=rem_suj_antes
        self.deduinca=deduinca
        self.deduincb=deduincb
        self.remsujaimp=remsujaimp        
    def __repr__(self):
        return str(self.__dict__)
        
class calculo:
    
    def __init__(self,tiporegistro,cuil,alicuota,alicuotasinhoras,impuestodeterminado,impuestoretenido,totalacuenta,saldo,actadebitos,
                 acuentaperc,acuentaturismo,acta27424,acta35a,acta35b,acta35c,acta35d,acta35e,actadebitosfondo,actaturismofuera):
        self.tiporegisto=tiporegistro
        self.cuil=cuil
        self.alicuota=alicuota
        self.alicuotasinhoras=alicuotasinhoras
        self.impuestodeterminado=impuestodeterminado
        self.impuestoretenido=impuestoretenido
        self.totalacuenta=totalacuenta
        self.saldo=saldo
        self.actadebitos=actadebitos
        self.acuentaperc=acuentaperc
        self.acuentaturismo=acuentaturismo
        self.acta27424=acta27424
        self.acta35a=acta35a
        self.acta35b=acta35b
        self.acta35c=acta35c
        self.acta35d=acta35d
        self.acta35e=acta35e
        self.actaimpfondos=actadebitosfondo
        self.actaturismofuera=actaturismofuera
    def __repr__(self):
        return str(self.__dict__)


    
class mywindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
        
                       
        self.ui.setupUi(self)
        self.ui.prima.setEnabled(False)
        
        self.ui.actionNuevo.triggered.connect(self.nuevo)
        self.ui.actionLeer.triggered.connect(self.abrefichero)
        self.ui.actionGuardar.triggered.connect(self.guardafichero)
        self.ui.actionCerrar.triggered.connect(self.cerrar)
        self.ui.actionAcercaDelGeneradorTxt.triggered.connect(self.acerca)
        
        self.ui.aceptar.clicked.connect(self.acepta_periodo)
        
        self.ui.calculo_2020.clicked.connect(self.calculo_anual_2020)
        self.ui.pushButton.clicked.connect(self.nuevo_empleado)
        self.ui.confirmar.clicked.connect(self.agregar_empleado)
        self.ui.listWidget.itemSelectionChanged.connect(self.cargar_empleado)
        self.ui.cuil.textChanged.connect(self.cambia_cuil)
        self.ui.pushButton_2.clicked.connect(self.elimina_empleados)
       #calulos gravada 
        self.ui.Bruto.textChanged.connect(self.cal_gravada)
        self.ui.No_habituales.textChanged.connect(self.cal_gravada)
        self.ui.SAC1grav.textChanged.connect(self.cal_gravada)
        self.ui.SAC2grav.textChanged.connect(self.cal_gravada)
        self.ui.viaticosgrav.textChanged.connect(self.cal_gravada)
        self.ui.docentesgrav.textChanged.connect(self.cal_gravada)
        self.ui.Bruto_2.textChanged.connect(self.cal_gravada)
        self.ui.No_habituales_2.textChanged.connect(self.cal_gravada)
        self.ui.SAC1grav_2.textChanged.connect(self.cal_gravada)
        self.ui.viaticosgrav_2.textChanged.connect(self.cal_gravada)
        self.ui.Hsgrav.textChanged.connect(self.cal_gravada)
        self.ui.docentesgrav_2.textChanged.connect(self.cal_gravada)
        self.ui.ajustesgrav.textChanged.connect(self.cal_gravada)
        self.ui.ajustesgrav_2.textChanged.connect(self.cal_gravada)
        self.ui.SAC2grav_2.textChanged.connect(self.cal_gravada)
        self.ui.Hsgrav_2.textChanged.connect(self.cal_gravada)
       #calulos exenta    
        self.ui.exenta.textChanged.connect(self.cal_exenta)
        self.ui.horasextr_ex.textChanged.connect(self.cal_exenta)
        self.ui.viaticos_ex.textChanged.connect(self.cal_exenta)
        self.ui.docentes_ex.textChanged.connect(self.cal_exenta)
        self.ui.exenta_2.textChanged.connect(self.cal_exenta)
        self.ui.horasextr_ex_2.textChanged.connect(self.cal_exenta)
        self.ui.viaticos_ex_2.textChanged.connect(self.cal_exenta)
        self.ui.docentes_ex_2.textChanged.connect(self.cal_exenta)
        self.ui.No_habituales_ext.textChanged.connect(self.cal_exenta)
        self.ui.No_habituales_ext_2.textChanged.connect(self.cal_exenta)
        self.ui.sac_exent.textChanged.connect(self.cal_exenta)
        self.ui.sac2exec.textChanged.connect(self.cal_exenta)
        self.ui.ajustes_ex.textChanged.connect(self.cal_exenta)
        self.ui.sac_exent_2.textChanged.connect(self.cal_exenta)
        self.ui.sac2exec_2.textChanged.connect(self.cal_exenta)
        self.ui.ajustes_ex_2.textChanged.connect(self.cal_exenta)
        self.ui.rem27549.textChanged.connect(self.cal_exenta)
        self.ui.rem27549_2.textChanged.connect(self.cal_exenta)
      #calulos deducciones
        self.ui.jubilacion.textChanged.connect(self.cal_deducciones)
        self.ui.obrasocial.textChanged.connect(self.cal_deducciones)
        self.ui.sindicato.textChanged.connect(self.cal_deducciones)
        self.ui.jubilacion_2.textChanged.connect(self.cal_deducciones)
        self.ui.obrasocial_2.textChanged.connect(self.cal_deducciones)
        self.ui.sindicato_2.textChanged.connect(self.cal_deducciones)
        self.ui.prima_2.textChanged.connect(self.cal_deducciones)
        self.ui.seguro.textChanged.connect(self.cal_deducciones)
        self.ui.seguro_retiro.textChanged.connect(self.cal_deducciones)
        self.ui.adquision.textChanged.connect(self.cal_deducciones)
        self.ui.seplio.textChanged.connect(self.cal_deducciones)
        self.ui.amortizacion.textChanged.connect(self.cal_deducciones)
        self.ui.descuentosley.textChanged.connect(self.cal_deducciones)
        self.ui.hipotecas.textChanged.connect(self.cal_deducciones)
        self.ui.CapitalSoc.textChanged.connect(self.cal_deducciones)
        self.ui.serviciodome.textChanged.connect(self.cal_deducciones)
        self.ui.alquiler.textChanged.connect(self.cal_deducciones)
        self.ui.viaticos.textChanged.connect(self.cal_deducciones)
        self.ui.indumentaria.textChanged.connect(self.cal_deducciones)
        self.ui.cuotamed.textChanged.connect(self.cal_deducciones)
        self.ui.fisco.textChanged.connect(self.cal_deducciones)
        self.ui.honorarios_serv.textChanged.connect(self.cal_deducciones)
      #otras
        self.ui.otras_actores.textChanged.connect(self.cal_deducciones)
        self.ui.otras_caja.textChanged.connect(self.cal_deducciones)
        self.ui.otras_fondo.textChanged.connect(self.cal_deducciones)
        self.ui.otras_jub.textChanged.connect(self.cal_deducciones)
        self.ui.Cajas_comp.textChanged.connect(self.cal_deducciones)
        
       #art23 
        self.ui.dedconyu.textChanged.connect(self.cal_deducciones_art23)
        self.ui.dedhijos.textChanged.connect(self.cal_deducciones_art23)
        self.ui.dedgni.textChanged.connect(self.cal_deducciones_art23)
        self.ui.dedespecial.textChanged.connect(self.cal_deducciones_art23)
        self.ui.dedesp.textChanged.connect(self.cal_deducciones_art23)
        
       #acta
        self.ui.actadebitos.textChanged.connect(self.cel_pago_a_cta)
        self.ui.actaretenciones.textChanged.connect(self.cel_pago_a_cta)
        self.ui.acta3819.textChanged.connect(self.cel_pago_a_cta)
        self.ui.actabono.textChanged.connect(self.cel_pago_a_cta)
        self.ui.actainca.textChanged.connect(self.cel_pago_a_cta)
        self.ui.actaincb.textChanged.connect(self.cel_pago_a_cta)
        self.ui.actac.textChanged.connect(self.cel_pago_a_cta)
        self.ui.actad.textChanged.connect(self.cel_pago_a_cta)
        self.ui.actae.textChanged.connect(self.cel_pago_a_cta)
        self.ui.imprete.textChanged.connect(self.cel_pago_a_cta)
        self.ui.acta3819_2.textChanged.connect(self.cel_pago_a_cta)
        self.ui.actadebitos_2.textChanged.connect(self.cel_pago_a_cta)
        self.ui.impdet.textChanged.connect(self.cel_pago_a_cta)
        self.ui.alicuota.setCurrentIndex(0)
        self.ui.alicshor.setCurrentIndex(0)
       
        
        
       
    def elimina_empleados(self):
        if (self.ui.listWidget.currentIndex().row()!=-1):
            
            mensaje=QMessageBox()
            mensaje.setWindowTitle("Advertencia")
            mensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            cuil=self.ui.listWidget.currentItem().text()
            mensaje.setText("Seguro de eliminar el cuil "+cuil+" ?")
            result = mensaje.exec_()
            if (result == QMessageBox.Ok):
                ##print ("falta poco")
                palabra="02"+cuil
                res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
                lista_txt_1357.pop(res[0])
                palabra="03"+cuil
                res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
                lista_txt_1357.pop(res[0])
                palabra="04"+cuil
                res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
                lista_txt_1357.pop(res[0])
                palabra="05"+cuil
                res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
                lista_txt_1357.pop(res[0])
                palabra="06"+cuil
                res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
                lista_txt_1357.pop(res[0])
                self.ui.listWidget.takeItem(self.ui.listWidget.currentIndex().row())
            # do yes-action.se fija si quedo vacio
                if (self.ui.listWidget.currentIndex().row()==-1):
                    self.ui.prima.setEnabled(True)
                    self.ui.prima.setTabVisible(1,False)
                    self.ui.prima.setTabVisible(2,False)
                    self.ui.prima.setTabVisible(3,False)
                    self.ui.prima.setTabVisible(4,False)
                    self.ui.prima.setTabVisible(5,False)
                    self.ui.prima.setTabVisible(6,False)
                    self.ui.prima.setTabEnabled(0,False)
                    self.inicializar_formulario()
                    self.ui.cuil.setText("")
                    self.ui.cuil.setEnabled(True)
                    
                    
                    
           
                 
                      
    def nuevo(self):
        global lista_txt_1357
        global cabecera1
        if cabecera1!="":
            global lista_txt_1357
            mensaje=QMessageBox()
            mensaje.setWindowTitle("Advertencia")
            mensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            mensaje.setText("Si no guardaste los datos se van a borrar, seguro de continuar ?")
            result = mensaje.exec_()
            if (result == QMessageBox.Ok):            
                self.ui.prima.setEnabled(False)

                self.inicializar_formulario()
                self.ui.cuil.setText("")
                self.ui.cuil.setEnabled(True)
                lista_txt_1357=[]
                cabecera1=""
                self.ui.listWidget.setCurrentRow(-1)
                self.ui.listWidget.clear()
                self.ui.cuit.setText("")
                self.ui.spinBox.setValue(0)
                self.ui.tipo_presen.setValue(0)
                self.ui.spinBox_6.setValue(2020)
                self.ui.comboBox_2.setCurrentIndex(0)
                
    
    
    
    
    def cambia_cuil(self):
        cuil=self.ui.cuil.text()
        valido=validar_cuit(cuil)
        if valido:
            cuil=self.ui.cuil.text()
            if  self.ui.listWidget.currentIndex().row()==-1:
                palabra="02"+cuil
                res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
                if res:
                    QMessageBox.about(self,"Error","El empleado ya esta ingresado")
                else:
                    self.ui.cuil_label.setText(cuil)
                    self.ui.prima.setTabVisible(1,True)
                    self.ui.prima.setTabVisible(2,True)
                    self.ui.prima.setTabVisible(3,True)
                    self.ui.prima.setTabVisible(4,True)
                    self.ui.prima.setTabVisible(5,True)
                    self.ui.prima.setTabVisible(6,True)
                    self.ui.cuil.setEnabled(False)
            
    def cerrar(self):
        mensaje=QMessageBox()
        mensaje.setWindowTitle("Advertencia")
        mensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mensaje.setText("Seguro que deseas salir ?")
        result = mensaje.exec_()
        if (result == QMessageBox.Cancel):
            return
     
        sys.exit()
        #exit()
    def acerca(self):
        mensaje="El siguiente programa vesion en desarrollo no esta testeada en su totalidad \n"
        mensaje=mensaje+"Por lo tanto es susceptible de contener errores. \n"
        mensaje=mensaje+"Por ahora no valida todos datos ni realiza control de topes \n"
        mensaje=mensaje+"Al ser una version en desarrollo todavia no hay un manual de ayuda"
        QMessageBox.about(self,"Nota",mensaje)
        
        
            
    
    
    
    def nuevo_empleado(self):
       
        
        if (self.ui.listWidget.currentIndex().row()!=-1):
            self.ui.listWidget.setCurrentRow(-1)
            self.inicializar_formulario()
            self.ui.prima.setTabVisible(1,False)
            self.ui.prima.setTabVisible(2,False)
            self.ui.prima.setTabVisible(3,False)
            self.ui.prima.setTabVisible(4,False)
            self.ui.prima.setTabVisible(5,False)
            self.ui.prima.setTabVisible(6,False)
            self.ui.prima.setTabEnabled(0,False)
        if (self.ui.cuil.text()==""):
            self.ui.prima.setTabEnabled(0,True)
            self.ui.cuil.setEnabled(True)        
            
            

    def abrefichero(self):
        global nombrearchivoguardado
        global cabecera1
        if cabecera1!="":
            mensaje=QMessageBox()
            mensaje.setWindowTitle("Advertencia")
            mensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            mensaje.setText("El fichero en que estas trabajando, no se guardo, seguro de continuar ?")
            result = mensaje.exec_()
            if (result == QMessageBox.Cancel):
                return
       
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"Abrir Archivo", "","All Files (*);;txt Files (*.txt)", options=options)
        if fileName:
            stop_words=open(fileName,'r') 
            lineas= [linea.strip() for linea in stop_words]
            exitos=0
            if (len (lineas[0]))==38:
                texto=str(lineas[0])
                self.ui.cuit.setText(texto[2:13])
                self.ui.spinBox_6.setValue(int(texto[13:17]))
                self.ui.tipo_presen.setValue(int(texto[17:19]))
                self.ui.spinBox.setValue(int(texto[19:21]))
                tipop=int(texto[32])
                #print (tipop)
                self.ui.comboBox_2.setCurrentIndex(tipop-1)
                cabecera1=lineas[0]
                self.ui.listWidget.clear()
            for linea in lineas[1:]:
                if linea[:2]=="02":
                    #print (len(linea))
                    if len(linea)==35:
                        self.ui.listWidget.addItem(linea[2:13]) 
                        exitos=exitos+1
                    else:
                        exitos=0
                        break
                    
            global lista_txt_1357
            if exitos!=0:
                lista_txt_1357=lineas[1:]
                QMessageBox.about(self,"OK","Datos Cargados")
                self.inicializar_formulario()
                self.ui.prima.setEnabled(True)
                self.ui.listWidget.setCurrentRow(0)
                self.cargar_empleado()
                
             
                
                
            else:
                QMessageBox.about(self,"Error","El archivo no corresponde al la version 4 del 1357")
                
                
   
    def guardafichero(self):
        
        nombrefichero="F1357."+self.ui.cuit.text()+"."+self.ui.spinBox_6.text()+str(self.ui.tipo_presen.text()).rjust(2,"0")+"00.00"+str(self.ui.spinBox.text()).rjust(2,"0")+".txt"
        options =  QtWidgets.QFileDialog.Options()
        options |=  QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ =  QtWidgets.QFileDialog.getSaveFileName(self,"Guardar F1357 Texto para Afip",nombrefichero,"Text Files (*.txt)", options=options)
        if fileName:
            #print(fileName)        
            f = open(fileName,"w")
            f.write(cabecera1+"\n")
            for i in lista_txt_1357:
                f.write(i+"\n")
            f.close()
            QMessageBox.about(self,"OK", "Fichero Guardado")
                                              
            
    def cal_gravada(self):
       
        total_gravad=(self.ui.Bruto.value()+self.ui.No_habituales.value()+self.ui.SAC1grav.value()+self.ui.SAC2grav.value()+
                  self.ui.viaticosgrav.value()+self.ui.docentesgrav.value()+self.ui.Bruto_2.value()+self.ui.No_habituales_2.value()
                  +self.ui.SAC1grav_2.value()+self.ui.viaticosgrav_2.value()+self.ui.Hsgrav.value()
                  +self.ui.docentesgrav_2.value()+self.ui.ajustesgrav.value()+self.ui.ajustesgrav_2.value()+self.ui.SAC2grav_2.value()
                  +self.ui.Hsgrav_2.value())
        
        decimal2=self.ui.Bruto.value()-int(self.ui.Bruto.value())
        decimal2=int(round(decimal2*100,0))
        entero=int(self.ui.Bruto.value())
        textentero=str(entero).rjust(13,"0")
        textdecimal=str(decimal2).rjust(2,"0")
        #print (textentero)
        #print (textdecimal)
        total_gravad=round(total_gravad,2)
        totalsinhoras=round(total_gravad-self.ui.Hsgrav.value()*.83,2)
        self.ui.ImpGrav.setText(str(total_gravad))
        self.ui.totalsinhoras.setText(str(totalsinhoras))
        self.cal_deducciones()
    
        return (total_gravad)
    
    
    
    def cal_exenta(self):
       
        total_exenta=(self.ui.exenta.value()+self.ui.horasextr_ex.value()+self.ui.viaticos_ex.value()+self.ui.docentes_ex.value()+
                      self.ui.exenta_2.value()+self.ui.horasextr_ex_2.value()+self.ui.viaticos_ex_2.value()+self.ui.docentes_ex_2.value()+
                      self.ui.No_habituales_ext.value()+self.ui.sac_exent.value()+self.ui.sac2exec.value()+self.ui.ajustes_ex.value()
                      +self.ui.No_habituales_ext_2.value()+self.ui.sac_exent_2.value()+self.ui.sac2exec_2.value()+self.ui.ajustes_ex_2.value()
                      +self.ui.rem27549.value()+self.ui.rem27549_2.value())
        texto=str(round(total_exenta,2))
        self.ui.impEx.setText(texto)
        self.cal_deducciones()
        
        return total_exenta
    
    
        
    def  cal_deducciones(self):
        total_otras_deducciones=(self.ui.otras_actores.value()+self.ui.otras_caja.value()+self.ui.otras_fondo.value()+self.ui.otras_jub.value()+self.ui.Cajas_comp.value())
        texto=str(round(total_otras_deducciones,2))
        self.ui.lbldedu.setText(texto)
        
        deducciones=(self.ui.jubilacion.value()+self.ui.obrasocial.value()+self.ui.sindicato.value()+self.ui.jubilacion_2.value()
                           +self.ui.obrasocial_2.value()+self.ui.sindicato_2.value()+self.ui.prima_2.value()+
                           self.ui.seguro.value()+self.ui.seguro_retiro.value()+self.ui.adquision.value()+self.ui.seplio.value()+
                           self.ui.amortizacion.value()+self.ui.descuentosley.value()+self.ui.hipotecas.value()+self.ui.CapitalSoc.value()
                           +self.ui.serviciodome.value()+self.ui.alquiler.value()+self.ui.viaticos.value()+self.ui.indumentaria.value()
                           +total_otras_deducciones)
        texto=str(round(deducciones,2))
        self.ui.dedganeta.setText(texto)
        gravada=round(float(self.ui.ImpGrav.text()),2)
        ganancia_neta=round(gravada-deducciones,2)
        texto=str(ganancia_neta)
        self.ui.ganneta.setText(texto)
        topegan=round(ganancia_neta*5/100,2)
        texto=str(topegan)
        self.ui.topegan.setText(texto)
        total_deducciones=round(deducciones+self.ui.cuotamed.value()+self.ui.fisco.value()+self.ui.honorarios_serv.value(),2)
        texto=str(total_deducciones)
        self.ui.dedgral.setText(texto)
        self.ui.lblTotalDeduc.setText(texto)
        self.cal_deducciones_art23()
                                                                                                                                         
    def  cal_deducciones_art23(self):
        cargas_familia=round(self.ui.dedconyu.value()+self.ui.dedhijos.value(),2)
        texto=str(cargas_familia)
        self.ui.dedcargfam.setText(texto)
        deducciones23=round(self.ui.dedgni.value()+self.ui.dedespecial.value()+self.ui.dedesp.value()+cargas_familia,2)
        texto=str(deducciones23)
        self.ui.dedart23.setText(texto)
        #calcular_rem_sujeta
        gravada=float(self.ui.ImpGrav.text())
        deducciones=float(self.ui.lblTotalDeduc.text())
        rem_suj=round(gravada-deducciones-deducciones23,2)
        gravadasinhoras=float(self.ui.totalsinhoras.text())
        rem_suj_sinhoras=round(gravadasinhoras-deducciones-deducciones23,2)
        if (rem_suj<0):
            rem_suj=0
        if (rem_suj_sinhoras<0):
            rem_suj_sinhoras=0            
        texto=str(rem_suj)
        texto2=str(rem_suj_sinhoras)
        self.ui.remsujimp.setText(texto)
        self.ui.remsujimp_2.setText(texto)
        self.ui.remsujsihex.setText(texto2)
        self.ui.remsujsihex_2.setText(texto2)
        
        self.cel_pago_a_cta()
        
    def cel_pago_a_cta(self):
        totalpagoacta=(self.ui.actadebitos.value()+self.ui.actaretenciones.value()+self.ui.acta3819.value()+self.ui.actabono.value()+
                       self.ui.actainca.value()+self.ui.actaincb.value()+self.ui.actac.value()+self.ui.actad.value()+self.ui.actae.value()
                       +self.ui.acta3819_2.value()+self.ui.actadebitos_2.value())
        totalpagoacta=round(totalpagoacta,2)
        texto=str(totalpagoacta)
        self.ui.totalacta.setText(texto)
        saldo=self.ui.impdet.value()-self.ui.imprete.value()-totalpagoacta
        saldo=(round(saldo,2))
        texto=str(saldo)
        self.ui.saldo.setText(texto)
    
    def calculo_anual_2020(self):
        rem_suj=float(self.ui.remsujimp.text())
        rem_suj_sinhoras=float(self.ui.remsujsihex.text())
        alicuota,fijo,excedente=calculo_alicuota(rem_suj)
        self.ui.alicuota.setCurrentIndex(calculoalic(str(alicuota)))
        alicuota,fijo,excedente=calculo_alicuota(rem_suj_sinhoras)
        impuesto=round(fijo+(rem_suj-excedente)/100*alicuota,2)
        self.ui.impdet.setValue(impuesto)
        self.ui.alicshor.setCurrentIndex(calculoalic(str(alicuota)))
                #self.ui.checkBox_4.setChecked(False)
    
        
    def acepta_periodo(self):
        global cabecera1
        cuit=self.ui.cuit.text()
        valido=validar_cuit(cuit)
        if valido:
            anual,final,informativa,distracto=False,False,False,False
            if self.ui.comboBox_2.currentIndex()==0:
                anual=True
                tipo="1"
            if self.ui.comboBox_2.currentIndex()==1:
                final=True
                tipo="2"
            if self.ui.comboBox_2.currentIndex()==2:    
                informativa=True
                tipo="3"
            if self.ui.comboBox_2.currentIndex()==3:    
                distracto=True
                tipo="4"
            if (anual==False and final==False and informativa==False and distracto==False):
                QMessageBox.about(self,"Error","Debe Seleccionar un tipo de liquidacion")
            else:
                if ((anual or distracto)
                    and self.ui.tipo_presen.value()!=0):
                    QMessageBox.about(self,"Error","Si es anual el mes tiene que ser 0")
                elif ((informativa or final)
                    and self.ui.tipo_presen.value()==0):
                    QMessageBox.about(self,"Error","Si es final/informativa el mes tiene que ser distino de 0")
                elif ((informativa or final)
                    and self.ui.spinBox_6.value()<2021):
                    QMessageBox.about(self,"Error","Si es final/informativa el periodo tiene que ser mayor al 2020")
                                    
                else:
                
                    self.ui.prima.setEnabled(True)
                    self.ui.prima.setTabVisible(1,False)
                    self.ui.prima.setTabVisible(2,False)
                    self.ui.prima.setTabVisible(3,False)
                    self.ui.prima.setTabVisible(4,False)
                    self.ui.prima.setTabVisible(5,False)
                    self.ui.prima.setTabVisible(6,False)
                    self.ui.prima.setTabEnabled(0,False)
                    QMessageBox.about(self,"OK","Datos Correctos")
                    self.inicializar_formulario()
                    self.ui.cuil.setText("")
                    #Carga empresa
                    cabecera1="01"+self.ui.cuit.text()+str(self.ui.spinBox_6.text()).rjust(2,"0")+str(self.ui.tipo_presen.text()).rjust(2,"0")+str(self.ui.spinBox.text()).rjust(2,"0")+"0103"+"215"+"1357"+tipo+"00400"
                               
                    
                    
        
                
                
        else:
            QMessageBox.about(self,"Error","Cuit No Valido")
    def inicializar_formulario(self):
        self.ui.cuil.setText("")
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        self.ui.checkBox_3.setChecked(False)
        self.ui.Bruto.setValue(0)
        self.ui.No_habituales.setValue(0)
        self.ui.SAC1grav.setValue(0)
        self.ui.SAC2grav.setValue(0)
        self.ui.viaticosgrav.setValue(0)
        self.ui.docentesgrav.setValue(0)
        self.ui.Bruto_2.setValue(0)
        self.ui.No_habituales_2.setValue(0)
        self.ui.SAC1grav_2.setValue(0)
        self.ui.viaticosgrav_2.setValue(0)
        self.ui.Hsgrav.setValue(0)
        self.ui.docentesgrav_2.setValue(0)
        self.ui.ajustesgrav.setValue(0)
        self.ui.ajustesgrav_2.setValue(0)
        self.ui.SAC2grav_2.setValue(0)
        self.ui.Hsgrav_2.setValue(0)
            #calulos exenta    
        self.ui.exenta.setValue(0)
        self.ui.horasextr_ex.setValue(0)
        self.ui.viaticos_ex.setValue(0)
        self.ui.docentes_ex.setValue(0)
        self.ui.exenta_2.setValue(0)
        self.ui.horasextr_ex_2.setValue(0)
        self.ui.viaticos_ex_2.setValue(0)
        self.ui.docentes_ex_2.setValue(0)
        self.ui.No_habituales_ext.setValue(0)
        self.ui.No_habituales_ext_2.setValue(0)
        self.ui.sac_exent.setValue(0)
        self.ui.sac2exec.setValue(0)
        self.ui.ajustes_ex.setValue(0)
        self.ui.sac_exent_2.setValue(0)
        self.ui.sac2exec_2.setValue(0)
        self.ui.ajustes_ex_2.setValue(0)
        self.ui.rem27549.setValue(0)
        self.ui.rem27549_2.setValue(0)
        #calulos deducciones
        self.ui.jubilacion.setValue(0)
        self.ui.obrasocial.setValue(0)
        self.ui.sindicato.setValue(0)
        self.ui.jubilacion_2.setValue(0)
        self.ui.obrasocial_2.setValue(0)
        self.ui.sindicato_2.setValue(0)
        self.ui.prima_2.setValue(0)
        self.ui.seguro.setValue(0)
        self.ui.seguro_retiro.setValue(0)
        self.ui.adquision.setValue(0)
        self.ui.seplio.setValue(0)
        self.ui.amortizacion.setValue(0)
        self.ui.descuentosley.setValue(0)
        self.ui.hipotecas.setValue(0)
        self.ui.CapitalSoc.setValue(0)
        self.ui.serviciodome.setValue(0)
        self.ui.alquiler.setValue(0)
        self.ui.viaticos.setValue(0)
        self.ui.indumentaria.setValue(0)
        self.ui.cuotamed.setValue(0)
        self.ui.fisco.setValue(0)
        self.ui.honorarios_serv.setValue(0)
            #otras
        self.ui.otras_actores.setValue(0)
        self.ui.otras_caja.setValue(0)
        self.ui.otras_fondo.setValue(0)
        self.ui.otras_jub.setValue(0)
        self.ui.Cajas_comp.setValue(0)
        
            #art23 
        self.ui.dedconyu.setValue(0)
        self.ui.dedhijos.setValue(0)
        self.ui.dedgni.setValue(0)
        self.ui.cant_hijos.setValue(0)
        self.ui.dedespecial.setValue(0)
        self.ui.dedesp.setValue(0)
        #calculo
        self.ui.actadebitos.setValue(0)
        self.ui.actaretenciones.setValue(0)
        self.ui.acta3819.setValue(0)
        self.ui.actabono.setValue(0)
        self.ui.actainca.setValue(0)
        self.ui.actaincb.setValue(0)
        self.ui.actac.setValue(0)
        self.ui.actad.setValue(0)
        self.ui.actae.setValue(0)
        self.ui.imprete.setValue(0)
        self.ui.acta3819_2.setValue(0)
        self.ui.actadebitos_2.setValue(0)
        self.ui.impdet.setValue(0)
        self.ui.alicuota.setCurrentIndex(0)
        self.ui.alicshor.setCurrentIndex(0)
    
    def agregar_empleado(self):
    #datos empleado
        texto1357=""
        cuil=self.ui.cuil.text()        
        desde=self.ui.spinBox_6.text()+str(self.ui.spinBox_2.text()).rjust(2,"0")+str(self.ui.spinBox_4.text()).rjust(2,"0")
        hasta=self.ui.spinBox_6.text()+str(self.ui.spinBox_3.text()).rjust(2,"0")+str(self.ui.spinBox_5.text()).rjust(2,"0")
        beneficio=str(self.ui.comboBox.currentIndex()+1)
        largadistancia=to_bool(self.ui.checkBox.isChecked())
        ley27424=to_bool(self.ui.checkBox_2.isChecked())
        ley27549=to_bool(self.ui.checkBox_3.isChecked())
        meses=str(self.ui.spinBox_3.value()-self.ui.spinBox_2.value()+1).rjust(2,"0")
        empleado=trabajador("02",cuil,desde,hasta,meses,beneficio,largadistancia,ley27424,ley27549)
        texto=convertir_a_cadena(empleado)
        #print (texto)
        
        if (self.ui.listWidget.currentIndex().row()!=-1):
            palabra="02"+cuil
            res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
            lista_txt_1357[res[0]]=texto
        else:
            lista_txt_1357.append(texto)
        
        
    #datos remuneracion
        tiporegistro="03"
        bruto=ctexto(13,2,self.ui.Bruto.value())
        nohabitualesgrava=ctexto(13,2,self.ui.No_habituales.value())
        sac1grav=ctexto(13,2,self.ui.SAC1grav.value())
        sac2grav=ctexto(13,2,self.ui.SAC2grav.value())
        hextgrav=ctexto(13,2,self.ui.Hsgrav.value())
        viaticosgrav=ctexto(13,2,self.ui.viaticosgrav.value())
        docentegrav=ctexto(13,2,self.ui.docentesgrav.value())
        exentasinhoras=ctexto(13,2,self.ui.exenta.value())
        exentahoras=ctexto(13,2,self.ui.horasextr_ex.value())
        viaticosexenta=ctexto(13,2,self.ui.viaticos_ex.value())
        docenteexenta=ctexto(13,2,self.ui.docentes_ex.value())
        otrosempleosbrutgrav=ctexto(13,2,self.ui.Bruto_2.value())
        otrosemplnohabigrav=ctexto(13,2,self.ui.No_habituales_2.value())
        otrosemplsac1grav=ctexto(13,2,self.ui.SAC1grav_2.value())
        otrosemplsac2grav=ctexto(13,2,self.ui.SAC2grav_2.value())
        otrosemplhsextgrav=ctexto(13,2,self.ui.Hsgrav_2.value())
        otrosempviaticosgrav=ctexto(13,2,self.ui.viaticosgrav_2.value())
        otrosempdocgrav=ctexto(13,2,self.ui.docentesgrav_2.value())
        otrosemplexcsinhoras=ctexto(13,2,self.ui.exenta_2.value())
        otrosexenthorasextra=ctexto(13,2,self.ui.horasextr_ex_2.value())
        otrosviaticosexe=ctexto(13,2,self.ui.viaticos_ex_2.value())
        otrosdocenexe=ctexto(13,2,self.ui.docentes_ex_2.value())
        gravada=float(self.ui.ImpGrav.text())
        nogravada=float(self.ui.impEx.text())
        remgravada=ctexto(13,2,gravada)
        remnogravada=ctexto(13,2,nogravada)
        totalremu=ctexto(15,2,gravada+nogravada)
        nohabitexe=ctexto(13,2,self.ui.No_habituales_ext.value())
        sac1exent=ctexto(13,2,self.ui.sac_exent.value())
        sec2exent=ctexto(13,2,self.ui.sac2exec.value())
        ajustesgrav=ctexto(13,2,self.ui.ajustesgrav.value())
        ajustesnoalcanzado=ctexto(13,2,self.ui.ajustes_ex.value())
        otrosajustesgrav=ctexto(13,2,self.ui.ajustesgrav.value())
        otrosajustesnoalcanzado=ctexto(13,2,self.ui.ajustes_ex_2.value())
        otrosnohabitualesexento=ctexto(13,2,self.ui.No_habituales_ext_2.value())
        otrossacexe=ctexto(13,2,self.ui.sac_exent_2.value())
        otrossac2exe=ctexto(13,2,self.ui.sac2exec_2.value())
        otrosajusgrav=ctexto(13,2,self.ui.ajustesgrav_2.value())
        otrosajusexe=ctexto(13,2,self.ui.ajustes_ex_2.value())
        ley27549=ctexto(13,2,self.ui.rem27549.value())
        otrosley27549=ctexto(13,2,self.ui.rem27549_2.value())
        regremun=renumeraciones(tiporegistro,cuil,bruto,nohabitualesgrava,sac1grav,sac2grav,hextgrav,viaticosgrav,docentegrav,exentasinhoras,exentahoras,viaticosexenta,
                                docenteexenta,otrosempleosbrutgrav,otrosemplnohabigrav,otrosemplsac1grav,otrosemplsac2grav,otrosemplhsextgrav,otrosempviaticosgrav,otrosempdocgrav,
                                otrosemplexcsinhoras,otrosexenthorasextra,otrosviaticosexe,otrosdocenexe,remgravada,remnogravada,totalremu,nohabitexe,sac1exent,sec2exent,
                                ajustesgrav,ajustesnoalcanzado,otrosajustesgrav,otrosajustesnoalcanzado,otrosnohabitualesexento,otrossacexe,otrossac2exe,otrosajusgrav,otrosajusexe,ley27549,
                                otrosley27549)
        lista_renumeraciones.append(regremun)
        texto=convertir_a_cadena(regremun)
        #print (texto)        
        #print (len(texto))
        
        
        if (self.ui.listWidget.currentIndex().row()!=-1):
            palabra="03"+cuil
            res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
            lista_txt_1357[res[0]]=texto
        else:
            lista_txt_1357.append(texto)        
        
        
        
        #deducciones generales
        tiporegistro="04"
        jubilacion=ctexto(13,2,self.ui.jubilacion.value())
        otrosjub=ctexto(13,2,self.ui.jubilacion_2.value())
        obrasocial=ctexto(13,2,self.ui.obrasocial.value())
        otrosobrasoc=ctexto(13,2,self.ui.obrasocial_2.value())
        sindicato=ctexto(13,2,self.ui.sindicato.value())
        otrossindicato=ctexto(13,2,self.ui.sindicato_2.value())
        cuotamedico=ctexto(13,2,self.ui.cuotamed.value())
        primasseguromuerte=ctexto(13,2,self.ui.prima_2.value())
        seguromixta=ctexto(13,2,self.ui.seguro.value())
        retiroprivado=ctexto(13,2,self.ui.seguro_retiro.value())
        adquisicion_cuotaparte=ctexto(13,2,self.ui.adquision.value())
        sepelio=ctexto(13,2,self.ui.seplio.value())
        amortizaciones=ctexto(13,2,self.ui.amortizacion.value())
        donaciones=ctexto(13,2,self.ui.fisco.value())
        descxley=ctexto(13,2,self.ui.descuentosley.value())
        honorariosasisten=ctexto(13,2,self.ui.honorarios_serv.value())
        interesescred=ctexto(13,2,self.ui.hipotecas.value())
        apcapsoc=ctexto(13,2,self.ui.CapitalSoc.value())
        otras_cajas=ctexto(13,2,self.ui.Cajas_comp.value())
        alquileres=ctexto(13,2,self.ui.alquiler.value())
        domestico=ctexto(13,2,self.ui.serviciodome.value())
        viaticosxempleador=ctexto(13,2,self.ui.viaticos.value())
        indumentaria=ctexto(13,2,self.ui.indumentaria.value())
        n_otrasdedu=float(self.ui.lbldedu.text())
        otrasdedu=ctexto(13,2,n_otrasdedu)
        n_totaldedu=float(self.ui.lblTotalDeduc.text())
        totaldedugral=ctexto(15,2,n_totaldedu)
        otras_aportjub=ctexto(13,2,self.ui.otras_jub.value())
        otras_cajasprov=ctexto(13,2,self.ui.otras_caja.value())
        otras_actores=ctexto(13,2,self.ui.otras_actores.value())
        otras_fondos=ctexto(13,2,self.ui.otras_fondo.value())
        registrodedu=deducciones(tiporegistro,cuil,jubilacion,otrosjub,obrasocial,otrosobrasoc,sindicato,otrossindicato,cuotamedico,primasseguromuerte,
                                 seguromixta,retiroprivado,adquisicion_cuotaparte,sepelio,amortizaciones,donaciones,descxley,honorariosasisten,interesescred,apcapsoc,
                                 otras_cajas,alquileres,domestico,viaticosxempleador,indumentaria,otrasdedu,totaldedugral,otras_aportjub,otras_cajasprov,
                                 otras_actores,otras_fondos)
        lista_deducciones.append(registrodedu)
        texto=convertir_a_cadena(registrodedu)
        if (self.ui.listWidget.currentIndex().row()!=-1):
            palabra="04"+cuil
            res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
            lista_txt_1357[res[0]]=texto
        else:
            lista_txt_1357.append(texto)        
        #print (texto)        
        #print (len(texto))
        #ded. art. 23
        
        tiporegistro="05"
        gni=ctexto(13,2,self.ui.dedgni.value())
        deduccion_especial=ctexto(13,2,self.ui.dedespecial.value())
        deduccion_especifica=ctexto(13,2,self.ui.dedesp.value())
        conyugue=ctexto(13,2,self.ui.dedconyu.value())
        cant_hijos=str(self.ui.cant_hijos.text()).rjust(2,"0")
        hijos=ctexto(13,2,self.ui.dedhijos.value())
        n_totalcargas=float(self.ui.dedcargfam.text())
        total_cargas=ctexto(13,2,n_totalcargas)
        n_dedu_art30=float(self.ui.dedart23.text())
        ded_art30=ctexto(13,2,n_dedu_art30)
        n_rem_suj_antes=float(self.ui.remsujimp.text())
        rem_suj_antes="000000000000000"
        deduinca="000000000000000"
        deduincb="000000000000000"
        remsujaimp=ctexto(13,2,n_rem_suj_antes)        
        dedart30=deducciones_art_23(tiporegistro,cuil,gni,deduccion_especial,deduccion_especifica,conyugue,cant_hijos,hijos,total_cargas,ded_art30,rem_suj_antes,
                                    deduinca,deduincb,remsujaimp)
        lista_deducciones_art23.append(dedart30)
        texto=convertir_a_cadena(dedart30)
        #print (texto)        
        #print (len(texto))
        if (self.ui.listWidget.currentIndex().row()!=-1):
            palabra="05"+cuil
            res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
            lista_txt_1357[res[0]]=texto
        else:
            lista_txt_1357.append(texto)        
        #calculo
        tiporegistro="06"
        alicuota=str(self.ui.alicuota.currentIndex())
        alicuotasinhoras=str(self.ui.alicshor.currentIndex())
        n_impuestodeterminado=self.ui.impdet.value()
        impuestodeterminado=ctexto(13,2,n_impuestodeterminado)
        impuestoretenido=ctexto(13,2,self.ui.imprete.value())
        n_total_a_cta=float(self.ui.totalacta.text())
        totalacuenta=ctexto(13,2,n_total_a_cta)
        n_saldo=float(self.ui.saldo.text())
        saldo=ctexto(13,2,n_saldo)
        actadebitos=ctexto(13,2,self.ui.actadebitos.value())
        acuentaperc=ctexto(13,2,self.ui.actaretenciones.value())
        acuentaturismo=ctexto(13,2,self.ui.acta3819.value())
        acta27424=ctexto(13,2,self.ui.actabono.value())
        acta35a=ctexto(13,2,self.ui.actainca.value())
        acta35b=ctexto(13,2,self.ui.actaincb.value())
        acta35c=ctexto(13,2,self.ui.actac.value())
        acta35d=ctexto(13,2,self.ui.actad.value())
        acta35e=ctexto(13,2,self.ui.actae.value())
        actadebitosfondo=ctexto(13,2,self.ui.actadebitos_2.value())
        actaturismofuera=ctexto(13,2,self.ui.acta3819_2.value())
        calcular_impuesto=calculo(tiporegistro,cuil,alicuota,alicuotasinhoras,impuestodeterminado,impuestoretenido,totalacuenta,saldo,actadebitos,
                                  acuentaperc,acuentaturismo,acta27424,acta35a,acta35b,acta35c,acta35d,acta35e,actadebitosfondo,actaturismofuera)
        lista_calculo.append(calcular_impuesto)
        texto=convertir_a_cadena(calcular_impuesto)
        #print (texto)        
        #print (len(texto))        
       
        if (self.ui.listWidget.currentIndex().row()!=-1):
            palabra="06"+cuil
            res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
            lista_txt_1357[res[0]]=texto
        else:
            lista_txt_1357.append(texto)
            self.ui.listWidget.addItem(cuil)
            self.inicializar_formulario()
            self.ui.prima.setTabVisible(1,False)
            self.ui.prima.setTabVisible(2,False)
            self.ui.prima.setTabVisible(3,False)
            self.ui.prima.setTabVisible(4,False)
            self.ui.prima.setTabVisible(5,False)
            self.ui.prima.setTabVisible(6,False)
            self.ui.prima.setTabEnabled(0,False)
        
        QMessageBox.about(self,"OK","Empleado Agregado/Modificado")
               
        
    def cargar_empleado(self):
        if self.ui.listWidget.currentIndex().row()!=-1:
            self.cargar_empleado_ok()
            #print (self.ui.listWidget.currentIndex().row())
    
    def cargar_empleado_ok(self):    
        global lista_txt_1357
        global cabecera1
        cuit=self.ui.listWidget.currentItem().text()
        #print ("seleccioneate"+cuit)
        palabra="02"+cuit
        res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
        texto=lista_txt_1357[res[0]]
        self.ui.cuil.setText(cuit)
        self.ui.cuil.setEnabled(False)
        self.ui.spinBox_2.setValue(int(texto[17:19]))
        self.ui.spinBox_4.setValue(int(texto[19:21]))
        self.ui.spinBox_3.setValue(int(texto[25:27]))
        self.ui.spinBox_5.setValue(int(texto[27:29]))
        self.ui.comboBox.setCurrentIndex(int(texto[31])-1)
        if int(texto[32])==1:
            self.ui.checkBox.setChecked(True)
        else:
            self.ui.checkBox.setChecked(False)
        if int(texto[33])==1:
            self.ui.checkBox_2.setChecked(True)
        else:
            self.ui.checkBox_2.setChecked(False)
        if  int(texto[34])==1:
            self.ui.checkBox_3.setChecked(True)
        else:
            self.ui.checkBox_3.setChecked(False)
        palabra="03"+cuit
        res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
        texto=lista_txt_1357[res[0]]  
        #print (len(texto))
            
        self.ui.Bruto.setValue(calvalor(texto[13:28]))
        self.ui.No_habituales.setValue(calvalor(texto[28:43]))
        self.ui.SAC1grav.setValue(calvalor(texto[43:58]))
        self.ui.SAC2grav.setValue(calvalor(texto[58:73]))
        self.ui.Hsgrav.setValue(calvalor(texto[73:88]))
        self.ui.viaticosgrav.setValue(calvalor(texto[88:103]))
        self.ui.docentesgrav.setValue(calvalor(texto[103:118]))
        self.ui.exenta.setValue(calvalor(texto[118:133]))
        self.ui.horasextr_ex.setValue(calvalor(texto[133:148]))
        self.ui.viaticos_ex.setValue(calvalor(texto[148:163]))
        self.ui.docentes_ex.setValue(calvalor(texto[163:178]))
        self.ui.Bruto_2.setValue(calvalor(texto[178:193]))
        self.ui.No_habituales_2.setValue(calvalor(texto[193:208]))
        self.ui.SAC1grav_2.setValue(calvalor(texto[208:223]))
        self.ui.SAC2grav_2.setValue(calvalor(texto[223:238]))
        self.ui.Hsgrav_2.setValue(calvalor(texto[238:253]))
        self.ui.viaticosgrav_2.setValue(calvalor(texto[253:268]))
        self.ui.docentesgrav_2.setValue(calvalor(texto[268:283]))
        self.ui.exenta_2.setValue(calvalor(texto[283:298]))
        self.ui.horasextr_ex_2.setValue(calvalor(texto[298:313]))
        self.ui.viaticos_ex_2.setValue(calvalor(texto[313:328]))
        self.ui.docentes_ex_2.setValue(calvalor(texto[328:343]))
        #gravada-343-358
        #nogravada 358-373
        #total 373-390
        self.ui.No_habituales_ext.setValue(calvalor(texto[390:405]))
        self.ui.sac_exent.setValue(calvalor(texto[405:420]))
        self.ui.sac2exec.setValue(calvalor(texto[420:435]))
        self.ui.ajustesgrav.setValue(calvalor(texto[435:450]))
        self.ui.ajustes_ex.setValue(calvalor(texto[451:465]))
        self.ui.No_habituales_ext_2.setValue(calvalor(texto[465:480]))
        self.ui.sac_exent_2.setValue(calvalor(texto[480:495]))
        self.ui.sac2exec_2.setValue(calvalor(texto[495:510]))
        self.ui.ajustesgrav_2.setValue(calvalor(texto[510:525]))
        self.ui.ajustes_ex_2.setValue(calvalor(texto[525:540]))
        self.ui.rem27549.setValue(calvalor(texto[540:555]))
        self.ui.rem27549_2.setValue(calvalor(texto[555:570]))
        
        #calulos deducciones
        palabra="04"+cuit
        res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
        texto=lista_txt_1357[res[0]]  
     
        self.ui.jubilacion.setValue(calvalor(texto[13:28]))
        self.ui.jubilacion_2.setValue(calvalor(texto[28:43]))
        self.ui.obrasocial.setValue(calvalor(texto[43:58]))
        self.ui.obrasocial_2.setValue(calvalor(texto[58:73]))
        self.ui.sindicato.setValue(calvalor(texto[73:88]))
        self.ui.sindicato_2.setValue(calvalor(texto[88:103]))
        self.ui.cuotamed.setValue(calvalor(texto[103:118]))
        self.ui.prima_2.setValue(calvalor(texto[118:133]))
        self.ui.seguro.setValue(calvalor(texto[133:148]))
        self.ui.seguro_retiro.setValue(calvalor(texto[148:163]))
        self.ui.adquision.setValue(calvalor(texto[163:178]))
        self.ui.seplio.setValue(calvalor(texto[178:193]))
        self.ui.amortizacion.setValue(calvalor(texto[193:208]))
        self.ui.fisco.setValue(calvalor(texto[208:223]))
        self.ui.descuentosley.setValue(calvalor(texto[223:238]))
        self.ui.honorarios_serv.setValue(calvalor(texto[238:253]))
        self.ui.hipotecas.setValue(calvalor(texto[253:268]))
        self.ui.CapitalSoc.setValue(calvalor(texto[268:283]))
        self.ui.Cajas_comp.setValue(calvalor(texto[283:298]))
        self.ui.alquiler.setValue(calvalor(texto[298:313]))
        self.ui.serviciodome.setValue(calvalor(texto[313:328]))
        self.ui.viaticos.setValue(calvalor(texto[328:343]))
        self.ui.indumentaria.setValue(calvalor(texto[343:358]))
           #otras-359-373
           #total-373-390
        self.ui.otras_jub.setValue(calvalor(texto[390:405]))
        self.ui.otras_caja.setValue(calvalor(texto[405:420]))
        self.ui.otras_actores.setValue(calvalor(texto[420:435]))
        self.ui.otras_fondo.setValue(calvalor(texto[435:450]))
       
        palabra="05"+cuit
        res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
        texto=lista_txt_1357[res[0]]         
        
            #art23 
            
       
        
        self.ui.dedgni.setValue(calvalor(texto[13:28]))
        self.ui.dedespecial.setValue(calvalor(texto[28:43]))
        self.ui.dedesp.setValue(calvalor(texto[43:58]))
        self.ui.dedconyu.setValue(calvalor(texto[58:73]))
        self.ui.cant_hijos.setValue(int(texto[73:75]))
        self.ui.dedhijos.setValue(calvalor(texto[75:90]))
        #calculo
        
        palabra="06"+cuit
        res= [indice for indice,string in enumerate(lista_txt_1357) if palabra in string]
        texto=lista_txt_1357[res[0]]  
        self.ui.alicuota.setCurrentIndex(int(texto[13]))
        self.ui.alicshor.setCurrentIndex(int(texto[14]))
        #print (calvalor(texto[15:30]))
        self.ui.impdet.setValue(calvalor(texto[15:30]))
        self.ui.imprete.setValue(calvalor(texto[30:45]))
        #act_tot 45-60,saldo 60,75
        self.ui.actadebitos.setValue(calvalor(texto[75:90]))
        self.ui.actaretenciones.setValue(calvalor(texto[90:105]))
        self.ui.acta3819.setValue(calvalor(texto[105:120]))
        self.ui.actabono.setValue(calvalor(texto[120:135]))
        self.ui.actainca.setValue(calvalor(texto[135:150]))
        self.ui.actaincb.setValue(calvalor(texto[150:165]))
        self.ui.actac.setValue(calvalor(texto[165:180]))
        self.ui.actad.setValue(calvalor(texto[180:195]))
        self.ui.actae.setValue(calvalor(texto[195:210]))
        self.ui.actadebitos_2.setValue(calvalor(texto[210:225]))
        self.ui.acta3819_2.setValue(calvalor(texto[225:240]))
        
       
        #esconde los tab
        self.ui.prima.setTabVisible(1,True)
        self.ui.prima.setTabVisible(2,True)
        self.ui.prima.setTabVisible(3,True)
        self.ui.prima.setTabVisible(4,True)
        self.ui.prima.setTabVisible(5,True)
        self.ui.prima.setTabVisible(6,True)
        self.ui.prima.setTabEnabled(0,True)        
        
    def closeEvent(self,event):
        mensaje=QMessageBox()
        mensaje.setWindowTitle("Advertencia")
        mensaje.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mensaje.setText("Seguro que deseas salir ?")
        result = mensaje.exec_()
        if (result == QMessageBox.Cancel):
            event.ignore()
        if result == QMessageBox.Ok:
            event.accept()    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    


        
            
    
def validar_cuit(cuit):
    # validaciones minimas
    if len(cuit) != 11 :
        return False
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]
    aux = 11 - (aux - (int(aux / 11) * 11))
    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9
    return aux == int(cuit[10])    

def calculo_alicuota(numero):
    alicuota=0
    fijo=0
    excente=0    
    if (numero>=0 and numero<=47669.16):
        alicuota=5
        fijo=0
        excente=0
    if (numero>47669.16 and numero<=95338.32):
        alicuota=9
        fijo=2383.46
        excente=47669.16        
    if (numero>95338.32 and numero<=143007.48):
        alicuota=12
        fijo=6673.68
        excente=95338.32
    if (numero>143007.48 and numero<=190676.65):    
        alicuota=15
        fijo=12393.98
        excente=143007.48
    if (numero>190676.65 and numero<=286014.96):         
        alicuota=19
        fijo=19544.36
        excente=190676.65
    if (numero>286014.96 and numero<=381353.28):
        alicuota=23
        fijo=37658.64
        excente=286014.96
    if (numero>381353.28 and numero<=572029.92):
        alicuota=27
        fijo=59586.45
        excente=381353.28
    if (numero>572029.92 and numero<=762706.57):
        alicuota=31
        fijo=111069.14
        excente=572029.92
    if (numero>762706.57):    
        alicuota=35
        fijo=170178.90
        excente=762706.57
    return(alicuota,fijo,excente)
def calculoalic(texto):
    numero=float(texto)
    numero=int(numero)
    valor=0
    if numero==0:
        valor=0
    if numero==5:
        valor=1
    if numero==9:
        valor=2
    if numero==12:
        valor=3
    if numero==15:
        valor=4
    if numero==19:
        valor=5
    if numero==23:
        valor=6
    if numero==27:
        valor=7
    if numero==31:
        valor=8
    if numero==35:
        valor=9
    return valor
        

def mid(empieza,termina,texto,cadena):
    textonuevo=""
    largo=len(texto)
    textonuevo=cadena[0:empieza-1]+texto+cadena[termina:]
    #print (textonuevo)
    return (textonuevo)
def to_bool(s):
    return "1" if s == True else "0"
def rellenarcero(numero):
    y=""
    for x in range(1,numero+1):
        y=y+"0"
    return y

def convertir_a_cadena(objeto):
    cadena=str(objeto).split(",")
    texto=""
    #print (cadena)
    #print (len(cadena))
    for x in range(len(cadena)):
        separador=cadena[x].find(":")
        inicio=cadena[x].find("'",separador)
        final=cadena[x].rfind("'")
        texto=texto+cadena[x][inicio:final]
    texto=texto.replace("'","")
    return texto
    
def ctexto(entero,decima,numero):
    decimal2=numero-int(numero)
    decimal2=int(round(decimal2*100,0))
    decimal2=abs(decimal2)
    entero2=int(numero)
    textentero=str(entero2).rjust(entero,"0")
    textdecimal=str(decimal2).rjust(decima,"0")
    texto=textentero+textdecimal
    return (texto)




def calvalor(texto):
    ##print(texto)
    entero=float(texto[:-2])
    decimal=round(float(texto[-2:])/100,2)
    numero=entero+decimal
    ##print (numero)
    return numero
    
                  
                 


app = QtWidgets.QApplication([])

app.setStyle("Fusion")
application = mywindow()
application.show()

sys.exit(app.exec())