import Foundation

class HalloWorld {
    init() {
        InitHalloWorld_Delegate(delegate: self)
    }
}

extension HalloWorld: HalloWorld_Delegate {

    func send_string(string: String) {
        print(string)
    }

}
