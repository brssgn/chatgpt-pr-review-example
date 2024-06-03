//
//  Utils.swift
//  PRReviewGAI
//
//  Created by Boris on 29.05.2024.
//

import Foundation

extension String {
    var integerValue: Int {
        Int(self)!
    }
}

extension Int {
    var stringValue: String {
        "\(self)"
    }
}

extension String {
    var zeroValue: String {
        return 0 as! String
    }
}
