def note2Freq(octave, semitone, cent, ref){
  note = (octave * 12) + semitone + (cent / 100)
  return ref * math.pow(2, (note - 33) / 12)
  }
  
def freq2Note(freq, ref){
  ratio = freq / ref
  note = (math.log(ratio) / math.log(2)) * 12
  return note + 33
  }
