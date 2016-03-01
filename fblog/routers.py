class fblogRouter(object):
    """
    A router to control all database operations on models in the
    fblog application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read fblog models go to fblog_db.
        """
        if model._meta.app_label == 'fblog':
            return 'fblog_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write fblog models go to fblog_db.
        """
        if model._meta.app_label == 'fblog':
            return 'fblog_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the fblog app is involved.
        """
        if obj1._meta.app_label == 'fblog' or \
           obj2._meta.app_label == 'fblog':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the fblog app only appears in the 'fblog_db'
        database.
        """
        if app_label == 'fblog':
            return db == 'fblog_db'
        return None