HalloWorld example
==================



Wrapper file:
*************
.. code-block:: python

    #



Swift:
******

.. code-block:: swift

    import Foundation

    class HalloWorld {
        var py: HalloWorldPyCallback!
        init() {
            InitHalloWorld_Delegate(delegate: self)
        }
    }

    extension HalloWorld: HalloWorld_Delegate {
        func set_HalloWorld_Callback(callback: AppleApiPyCallback, cython_class: CythonClass) {
            py = callback
        }
        

        func hello_world(string: String) {
            print(string)
        }
        
    }

Api:
******

.. autoclass:: hallo_world.HalloWorld
    :members:

.. autoclass:: hallo_world.HalloWorld.Callbacks
    :members:



        
        
