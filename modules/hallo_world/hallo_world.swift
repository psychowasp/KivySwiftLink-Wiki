import Foundation

class HalloWorld {
    var py: HalloWorldPyCallback!
    init() {
        InitHalloWorld_Delegate(delegate: self)
    }
}

extension HalloWorld: HalloWorld_Delegate {
    func set_HalloWorld_Callback(callback: HalloWorldPyCallback, cython_class: CythonClass) {
        py = callback
    }


    func hello_world(string: String) {
        print(string)
    }

}
