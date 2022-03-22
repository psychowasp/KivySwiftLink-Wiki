import Foundation

class HalloWorld {
    init() {
        InitHalloWorld_Delegate(delegate: self)
    }
}

extension HalloWorld: HalloWorld_Delegate {

    func hello_world(string: String) {
        print(string)
    }

}
