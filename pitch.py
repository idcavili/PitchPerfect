def note2Freq(octave, semitone, cent, ref)
  note = (octave * 12) + semitone + (cent / 100)
  return ref * math.pow(2, (note - 33) / 12)
  
def freq2Note(freq, ref)
  ratio = freq / ref
  note = (math.log(ratio) / math.log(2)) * 12
  return note + 33
  
def pitchOffset(desired, actual)
  ratio = desired / actual
  return (math.log(ratio) / math.log(2)) *12
  
def semitone(freq, ref)
  return math.floor(freq2Note(freq, ref)) + 36
  
def onKeyMove(num, pos)
  if pos < thresh && note[num] == 0
    lastPos = pos
    lastTime = getTime()
  elif pos > thresh && note[num] == 0
    deltaPos = pos - lastPos
    deltaTime = getTime() - lastTime
    vel = deltaPos / deltaTime
    note[num] = 1
    noteOn(num, vel)
  elif pos > thresh && note[num] == 1
    lastPos = pos
    lastTime = getTime()
  elif pos < thresh && note[num] == 1
    deltaPos = pos - lastPos
    deltaTime - getTime() - lastTime
    vel = deltaPos / deltaTime
    note[num] = 1
    noteOff(num, vel)
    
