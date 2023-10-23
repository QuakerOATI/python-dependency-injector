Async Monitoring Daemon
=======================

A daemon that monitors Web service availability using a simple polling technique.

Project creation
----------------

#. Create directory structure and config files
#. Specify dependencies
#. Specify build and deployment process in Dockerfile
#. Define container in compose.yaml
#. Test scaffolding by running :code:`podman-compose build`

  .. note::
     If this fails due to "permission denied" errors, the problem is likely SELinux.  A quick, general fix is to set SELinux to "permissive" mode.  A less risky solution is to append :z or :Z to the "volumes" attributes of each service; see `this blog post <https://blog.ryanmartin.me/selinux-containers>`_.

#. Setup logging and config parsing
  - Place :code:`config` and :code:`logging` providers in containers.py
  - Use Configuration provider for config
  - Use Resource (i.e., singleton) provider for logging
#. Setup entrypoint structure
  - Instantiate container under :code:`__name__ == "__main__"` guard
#. Implement dispatcher and add to container as Factory provider

Architecture
------------

The app consists of a series of :code:`Monitor` objects scheduled and managed by a :code:`Dispatcher`.  Concrete :code:`Monitor` instances must be instantiated from a subclass of the abstract :code:`Monitor` class.

- For example: :code:`HttpMonitor` extends :code:`Monitor`, verifying the availability of a Web service by sending an HTTP request to a specified URL (the actual request is delegated to an :code:`HttpClient`).
