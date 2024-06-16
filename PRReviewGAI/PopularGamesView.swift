//
//  PopularGamesView.swift
//  PRReviewGAI
//
//  Created by Boris on 16.06.2024.
//

import SwiftUI

struct PopularGamesView: View {
    let games: [VideoGame]

    var body: some View {
        NavigationView {
            List(games) { game in
                HStack {
                    VStack(alignment: .leading) {
                        Text(game.name)
                            .font(.headline)
                        Text("Rating: \(game.rating, specifier: "%.1f")")
                            .font(.subheadline)
                            .foregroundColor(.gray)
                    }
                }
            }
            .navigationTitle("Popular Games")
        }
    }
}

struct PopularGamesView_Previews: PreviewProvider {
    static var previews: some View {
        PopularGamesView(games: VideoGame.sampleGames)
    }
}
