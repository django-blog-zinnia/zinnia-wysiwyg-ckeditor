=======================
zinnia-wysiwyg-ckeditor
=======================

Zinnia-wysiwyg-ckeditor is a package allowing you to edit your entries
with `CKEditor`_.

Installation
============

* Install the package on your system: ::

  $ pip install zinnia-wysiwyg-ckeditor

  `django-ckeditor`_ will also be installed as a dependency.
  
* Install and configure django-ckeditor if not already done. 

* Register the ``'zinnia_ckeditor'`` in your ``INSTALLED_APPS`` after the
  ``'zinnia'`` application.

You are done !

Configuration
=============

You can customize the CKEditor instance by defining a ``zinnia-content``
configuration into the ``CKEDITOR_CONFIGS`` setting.

If the ``zinnia-content`` configuration is not found, the ``default``
configuration will be used.

Example of configuration: ::

  CKEDITOR_CONFIGS = {
      'default': {
          'toolbar': 'Full',
      },
      'zinnia-content': {
          'toolbar_Zinnia': [
              ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
              ['Undo', 'Redo'],
              ['Scayt'],
              ['Link', 'Unlink', 'Anchor'],
              ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
              ['Source'],
              ['Maximize'],
              '/',
              ['Bold', 'Italic', 'Underline', 'Strike',
               'Subscript', 'Superscript', '-', 'RemoveFormat'],
              ['NumberedList', 'BulletedList', '-',
               'Outdent', 'Indent', '-', 'Blockquote'],
              ['Styles', 'Format'],
          ],
          'toolbar': 'Zinnia',
      },
  }

.. _CKEditor: http://ckeditor.com/
.. _django-ckeditor: https://github.com/shaunsephton/django-ckeditor/
