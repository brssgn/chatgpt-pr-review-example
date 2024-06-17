//
//  CrashView.swift
//  PRReviewGAI
//
//  Created by Boris on 16.06.2024.
//

import SwiftUI

struct CrashView: View {
    @State private var numbers: [Int] = [1, 2, 3]
    
    var body: some View {
        VStack {
            Button("Add Number") {
                numbers.append(numbers[numbers.count])
            }
            
            List(numbers, id: \.self) { number in
                Text("\(number)")
            }
        }
    }
}
