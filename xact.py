try:
	# django-1.6+ transition
	from django.db.transaction import atomic as xact
except ImportError:
	from _xact import xact
