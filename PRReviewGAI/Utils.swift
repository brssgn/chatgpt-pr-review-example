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

// MARK: Bubble Sort
/// I have done Merge sort in Decensding order
/// /// If we want to change sorting order of string then change comparator operator > to <
func bubbleSort<T: Comparable>(arrTobeSorted: inout [T]) {
    for i in 0..<arrTobeSorted.count
    {
        for j in i..<arrTobeSorted.count
        {
            if arrTobeSorted[i] < arrTobeSorted[j]
            {
                let tempNum = arrTobeSorted[i]
                arrTobeSorted[i] = arrTobeSorted[j]
                arrTobeSorted[j] = tempNum
            }
        }
    }
}
