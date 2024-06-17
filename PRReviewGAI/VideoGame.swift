//
//  VideoGame.swift
//  PRReviewGAI
//
//  Created by Boris on 16.06.2024.
//

import Foundation

struct VideoGame: Identifiable {
    let id = UUID()
    let name: String
    let rating: Double
}

extension VideoGame {
    static let sampleGames = [
        VideoGame(name: "The Legend of Zelda: Breath of the Wild", rating: 4.9),
        VideoGame(name: "The Witcher 3: Wild Hunt", rating: 4.8),
        VideoGame(name: "Red Dead Redemption 2", rating: 4.7),
        VideoGame(name: "Super Mario Odyssey", rating: 4.8),
        VideoGame(name: "God of War", rating: 4.9)
    ]
}
