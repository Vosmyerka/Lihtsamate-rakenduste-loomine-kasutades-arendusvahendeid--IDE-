use_bpm 120
define :main do                                       # Main thing
  use_synth :piano
  
  play_pattern_timed [:d3, :d3, :d4], [0.25]
  sleep 0.225
  play_pattern_timed [:a3], [0.45]
  sleep 0.225
  play_pattern_timed [:gs3, :g3, :f3], [0.45]
  play_pattern_timed [:d3, :f3, :g3], [0.25]
  
  play_pattern_timed [:c3, :c3, :d4], [0.25]
  sleep 0.225
  play_pattern_timed [:a3], [0.45]
  sleep 0.225
  play_pattern_timed [:gs3, :g3, :f3], [0.45]
  play_pattern_timed [:d3, :f3, :g3], [0.25]
  
  play_pattern_timed [:b2, :b2, :d4], [0.25]
  sleep 0.225
  play_pattern_timed [:a3], [0.45]
  sleep 0.225
  play_pattern_timed [:gs3, :g3, :f3], [0.45]
  play_pattern_timed [:d3, :f3, :g3], [0.25]
  
  play_pattern_timed [:as2, :as2, :d4], [0.25]
  sleep 0.225
  play_pattern_timed [:a3], [0.45]
  sleep 0.225
  play_pattern_timed [:gs3, :g3, :f3], [0.45]
  play_pattern_timed [:d3, :f3, :g3], [0.25]
end

define :main2 do                                       # Main2 thing
  use_synth :piano
  
  play_pattern_timed [:d4, :d4, :d5], [0.25]
  sleep 0.225
  play_pattern_timed [:a4], [0.45]
  sleep 0.225
  play_pattern_timed [:gs4, :g4, :f4], [0.45]
  play_pattern_timed [:d4, :f4, :g4], [0.25]
  
  play_pattern_timed [:c4, :c4, :d5], [0.25]
  sleep 0.225
  play_pattern_timed [:a4], [0.45]
  sleep 0.225
  play_pattern_timed [:gs4, :g4, :f4], [0.45]
  play_pattern_timed [:d4, :f4, :g4], [0.25]
  
  play_pattern_timed [:b3, :b3, :d5], [0.25]
  sleep 0.225
  play_pattern_timed [:a4], [0.45]
  sleep 0.225
  play_pattern_timed [:gs4, :g4, :f4], [0.45]
  play_pattern_timed [:d4, :f4, :g4], [0.25]
  
  play_pattern_timed [:as3, :as3, :d5], [0.25]
  sleep 0.225
  play_pattern_timed [:a4], [0.45]
  sleep 0.225
  play_pattern_timed [:gs4, :g4, :f4], [0.45]
  play_pattern_timed [:d4, :f4, :g4], [0.25]
end

define :re2 do                                        # Re2 thing
  use_synth :piano
  
  play_pattern_timed [:d2, :d2], [0.45], amp: 1
  play_pattern_timed [:d2, :d2], [0.25], amp: 1
  sleep 0.25
  play_pattern_timed [:d2, :d2], [0.45], amp: 1
  play_pattern_timed [:d2, :d2, :d2, :d2], [0.25], amp: 1
  sleep 0.25
  
end

define :do2 do                                        # Do2 thing
  use_synth :piano
  
  play_pattern_timed [:c2, :c2], [0.45], amp: 1
  play_pattern_timed [:c2, :c2], [0.25], amp: 1
  sleep 0.25
  play_pattern_timed [:c2, :c2], [0.45], amp: 1
  play_pattern_timed [:c2, :c2, :c2, :c2], [0.25], amp: 1
  sleep 0.25
  
end

define :si1 do                                        # Si1 thing
  use_synth :piano
  
  play_pattern_timed [:b1, :b1], [0.45], amp: 1
  play_pattern_timed [:b1, :b1], [0.25], amp: 1
  sleep 0.25
  play_pattern_timed [:b1, :b1], [0.45], amp: 1
  play_pattern_timed [:b1, :b1, :b1, :b1], [0.25], amp: 1
  sleep 0.25
  
end

define :gs1 do                                        # Gs1 thing
  use_synth :piano
  
  play_pattern_timed [:gs1, :gs1], [0.45], amp: 1
  play_pattern_timed [:gs1, :gs1], [0.25], amp: 1
  sleep 0.25
  play_pattern_timed [:c2, :c2], [0.45], amp: 1
  play_pattern_timed [:c2, :c2, :c2, :c2], [0.25], amp: 1
  sleep 0.25
  
end

#--------------------------------------------------------

main

in_thread do
  main
end

in_thread do
  re2
  do2
  si1
  gs1
end

sleep 15                                             # End of part 1

in_thread do
  main
end

in_thread do
  main2
end

in_thread do
  re2
  do2
  si1
  gs1
end

sleep 15                                      # I have no idea how to loop that thing

in_thread do
  main
end

in_thread do
  main2
end

in_thread do
  re2
  do2
  si1
  gs1
end

# Too lazy to continue. Maybe some day...
# ⡆⣐⢕⢕⢕⢕⢕⢕⢕⢕⠅⢗⢕⢕⢕⢕⢕⢕⢕⠕⠕⢕⢕⢕⢕⢕⢕⢕⢕⢕
# ⢐⢕⢕⢕⢕⢕⣕⢕⢕⠕⠁⢕⢕⢕⢕⢕⢕⢕⢕⠅⡄⢕⢕⢕⢕⢕⢕⢕⢕⢕
# ⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕
# ⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕
# ⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑
# ⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐
# ⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐
# ⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔
# ⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕
# ⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕
# ⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕
# ⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕⢕⢕
# ⣆⢕⠄⢱⣄⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢁⢕⢕⠕⢁
# ⣿⣦⡀⣿⣿⣷⣶⣬⣍⣛⣛⣛⡛⠿⠿⠿⠛⠛⢛⣛⣉⣭⣤⣂⢜⠕⢑⣡⣴⣿