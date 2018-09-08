//
//  ResultsViewController.swift
//  FaceMatch
//
//  Created by Berchenko, Amiel D on 9/7/18.
//  Copyright © 2018 Berchenko, Amiel D. All rights reserved.
//

import UIKit

class ResultsViewController: UIViewController {
    
    // MARK: Properties
    
    @IBOutlet weak var samplePicture: UIImageView!
    @IBOutlet weak var yourImageView: UIImageView!
    @IBOutlet weak var percentMatchLabel: UILabel!
    @IBOutlet weak var pointsAddLabel: UILabel!
    @IBOutlet weak var totalPointsLabel: UILabel!

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */
    
    // MARK: Actions
    
    @IBAction func nextPressed(_ sender: UIButton) {
    }
    
    @IBAction func endPressed(_ sender: UIButton) {
    }
    

}
