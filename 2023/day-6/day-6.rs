use std::fs::File;
use std::io::{ BufReader, BufRead };

fn main() {
    let file = File::open("input.txt").expect("Input file missing!");
    let reader = BufReader::new(file);
    let lines: Vec<String> = reader.lines().collect::<Result<_, _>>().unwrap();

    //////////////////
    //    Part 1    //
    //////////////////

    let race_times: &Vec<i32> = &lines[0].trim().split(":").collect::<Vec<_>>()[1].split(" ").collect::<Vec<_>>().iter().filter(|&time| time != &"").map(|time| time.parse::<i32>().unwrap()).collect();

    let race_dists: &Vec<i32> = &lines[1].trim().split(":").collect::<Vec<_>>()[1].split(" ").collect::<Vec<_>>().iter().filter(|&time| time != &"").map(|time| time.parse::<i32>().unwrap()).collect();

    let races = race_times.iter().zip(race_dists.iter());

    let mut answer = 1;

    for (race_time, race_dist) in races {
        let mut ways_to_beat = 0;

        for charge_time in 0..*race_time {
            let speed = charge_time;
            let moving_time = race_time - charge_time;

            if speed * moving_time > *race_dist {
                ways_to_beat += 1;
            }
        }

        answer *= ways_to_beat;
    }

    println!("Part 1: {}", answer);

    //////////////////
    //    Part 2    //
    //////////////////

    let race_time: i64 = lines[0].trim().split(":").collect::<Vec<_>>()[1].replace(" ", "").parse::<i64>().unwrap();
    let race_dist: i64 = lines[1].trim().split(":").collect::<Vec<_>>()[1].replace(" ", "").parse::<i64>().unwrap();

    let mut first_beat: i64 = 0;

    for charge_time in 0..race_time {
        let speed = charge_time;
        let moving_time = race_time - charge_time;

        if speed * moving_time > race_dist {
            first_beat = charge_time;
            break;
        }
    }

    println!("Part 2: {}", race_time - ( first_beat *  2 ) + 1);
}
