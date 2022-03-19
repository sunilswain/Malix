malix.utils package
===================

Submodules
----------

malix.utils.Methods module
++++++++++++++++++++++++++

.. automodule:: malix.utils.Methods
   :members:
   :undoc-members:
   :show-inheritance:

malix.utils.attributes module
+++++++++++++++++++++++++++++

.. automodule:: malix.utils.attributes
   :members:
   :show-inheritance:

   .. py:class:: Account(data: dict)

      .. py:attribute:: json

         Formatted reponse(*str*).
      .. py:attribute:: response

         Raw response(*dict*).
      .. py:attribute:: id

         Id of the account.
      .. py:attribute:: adress

         Adress of the account.
      .. py:attribute:: isDisabled

         Tells whether the account is disabled or not.
      .. py:attribute:: isDeleted

         Tells whether the account is deleted or not.
      .. py:attribute:: quota

         Honestly, don't know.! may become useful in the future.
      .. py:attribute:: used

         Tells how many times used.
      .. py:attribute:: createdAt

         Tells when the account resource was created.
      .. py:attribute:: updatedAt

         Tells when the account resource was updated.


   .. py:class:: Domain(data: dict)

      .. py:attribute:: json

         Formatted reponse(*str*).
      .. py:attribute:: response

         Raw response(*dict*).
      .. py:attribute:: id

         Id of the domain.
      .. py:attribute:: domain

         domain of the :class:`Domain <malix.utils.attributes.Domain>` object.
      .. py:attribute:: isActive

         Tells whether the domain is still active or not.
      .. py:attribute:: isPrivate

         Tells whether the domain has been protected or not.
      .. py:attribute:: createdAt

         Tells when the domain resource was created.
      .. py:attribute:: updatedAt

         Tells when the domain resource was updated.

   .. py:class:: Message(data: dict)

      .. py:attribute:: json

         Formatted reponse(*str*).
      .. py:attribute:: response

         Raw response(*dict*).
      .. py:attribute:: id

         Id of the message.
      .. py:attribute:: accountId

         Account id of the cleint.
      .. py:attribute:: From

         Dictonary containing address and name of the sender.
      .. py:attribute:: To

         Dictonary containing address and name(will be hidden) of the receiver.
      .. py:attribute:: CC

         don't know ¯\_(ツ)_/¯
      .. py:attribute:: BCC

         don't know ¯\_(ツ)_/¯
      .. py:attribute:: subject

         subject of the message.
      .. py:attribute:: seen

         True if seen is updated using :func:`update_message <malix.client.Client.update_message()>`.
      .. py:attribute:: flagged

         Tells whether the message has been flagged or not.
      .. py:attribute:: isDeleted

         True if the message resource has been deleted.
      .. py:attribute:: verifications

         verifications list.
      .. py:attribute:: retention

         True if the message is still retained.
      .. py:attribute:: retentionDate

         The date of retention.
      .. py:attribute:: text

         Text of the message.
      .. py:attribute:: html

         html of the message.
      .. py:attribute:: hasAttachments

         True if the message contains attachments.
      .. py:attribute:: attachments

         The attachments of the message.
      .. py:attribute:: size

         size of the message in Bytes.
      .. py:attribute:: downloadUrl

         The download url of the message.
      .. py:attribute:: createdAt

         Tells when the message resource was created.
      .. py:attribute:: updatedAt

         Tells when the message resource was updated.


   .. py:class:: Token(data: dict)

      .. py:attribute:: id

         Id of the account.
      .. py:attribute:: token

         Token of the account.
      .. py:attribute:: json

         Formatted reponse(*str*).
      .. py:attribute:: response

         Raw response(*dict*).
      

malix.utils.exceptions module
+++++++++++++++++++++++++++++

.. automodule:: malix.utils.exceptions
   :members:
   :undoc-members:
   :show-inheritance:

malix.utils.headers module
++++++++++++++++++++++++++

.. automodule:: malix.utils.headers
   :members:
   :undoc-members:
   :show-inheritance:

malix.utils.jwtoken module
++++++++++++++++++++++++++

.. automodule:: malix.utils.jwtoken
   :members:
   :undoc-members:
   :show-inheritance:
