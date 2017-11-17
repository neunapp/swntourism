from django.db import models

class PackageManager(models.Manager):
    """procedimiento para tabla package"""

    def filter_package(self):
        """consulta para paquetes mas visitados"""

        return self.order_by('-visit')[:10]