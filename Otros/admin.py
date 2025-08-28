from django.contrib import admin
from .models import Cliente,Empleado,Servicio,Horario,Turno,ServicioXTurno,Producto,Stock,Caja,Venta,DetalleVenta,MetodoPago,Pago,Comprobante

# Register your models here.
# vista del admin para tener todos los modelos ahi perro

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display =('dni','nombre','apellido','telefono','email','fecha_registro','notas','activo')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('usuario','dni','nombre','apellido','telefono','especialidad','activo')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','precio','duracion_minutos','activo')

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display=('dia_semana','hora_inicio','hora_inicio','hora_fin','activo')

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('cliente','empleado','fecha','hora','estado')

@admin.register(ServicioXTurno)
class ServicioXTurnoAdmin(admin.ModelAdmin):
    list_display = ('turno','servicio','precio','activo')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','precio','stock_actual','imagen','activo')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display=('producto','cantidad','tipo_movimiento','fecha','observacion','activo')

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):
    list_display=('empleado','fecha_apertura','fecha_cierre','saldo_inicial','saldo_final','abierta')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente','empleado','fecha','total','caja','activo')

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('venta','producto','cantidad','precio_unitario','subtotal','activo')

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','activo')

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('venta','metodo_pago','monto','fecha','activo')

@admin.register(Comprobante)
class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('venta','tipo','numero','fecha_emision','activo')