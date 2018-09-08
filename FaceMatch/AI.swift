//
//  Model.swift
//  FaceMatch
//
//  Created by Berchenko, Amiel D on 9/8/18.
//  Copyright © 2018 Berchenko, Amiel D. All rights reserved.
//

import Foundation
import UIKit

protocol AI {
    func generateSampleImage() -> UIImage
    func checkMatch(sampleImage: UIImage, userImage: UIImage) -> Double
}
