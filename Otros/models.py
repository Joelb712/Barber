from django.db import models
from django.conf import settings

# Create your models here.

# --- CLIENTES ---
class Cliente(models.Model):
    dni=models.IntegerField(max_length=11,unique=True,blank=False,null=False,verbose_name="DNI / Documento")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# --- EMPLEADOS ---
class Empleado(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dni=models.IntegerField(max_length=11,unique=True,blank=False,null=False,verbose_name="DNI / Documento")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.get_full_name()


# --- SERVICIOS ---
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_minutos = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# --- HORARIOS ---
class Horario(models.Model):
    dia_semana = models.CharField(max_length=15)  # Ej: Lunes, Martes...
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.dia_semana} {self.hora_inicio} - {self.hora_fin}"


# --- TURNOS ---
class Turno(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(
        max_length=20,
        choices=[('pendiente', 'Pendiente'), ('confirmado', 'Confirmado'), ('cancelado', 'Cancelado'), ('completado', 'Completado')],
        default='pendiente'
    )

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.cliente}"


# --- SERVICIOS X TURNOS ---
class ServicioXTurno(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.turno} - {self.servicio}"


# --- PRODUCTOS ---
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock_actual = models.PositiveIntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# --- STOCK ---
class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo_movimiento = models.CharField(
        max_length=10,
        choices=[('entrada', 'Entrada'), ('salida', 'Salida')]
    )
    fecha = models.DateTimeField(auto_now_add=True)
    observacion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.tipo_movimiento} {self.cantidad} - {self.producto}"


# --- CAJAS ---
class Caja(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    fecha_apertura = models.DateTimeField()
    fecha_cierre = models.DateTimeField(blank=True, null=True)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    abierta = models.BooleanField(default=True)

    def __str__(self):
        return f"Caja {self.id} - {self.fecha_apertura.date()}"


# --- VENTAS ---
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    caja = models.ForeignKey(Caja, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"Venta {self.id} - {self.fecha.date()}"


# --- DETALLE DE VENTA ---
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.producto} x{self.cantidad}"


# --- MÉTODOS DE PAGO ---
class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


# --- PAGOS ---
class Pago(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.metodo_pago} - ${self.monto}"


# --- COMPROBANTES ---
class Comprobante(models.Model):
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=[('factura', 'Factura'), ('ticket', 'Ticket')])
    numero = models.CharField(max_length=50)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo} {self.numero}"