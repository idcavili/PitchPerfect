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
    attackVel[num] = vel
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
  elif pos => atThresh
    lastPos = pos
    setAT(num, pos - atThresh)
  elif pos < atThresh && lastPos => atThresh
    setAT(0)
    
def noteOn(num, vel)
  for(i=0;i<sizeof(zones);i+1)
    zone = zones.getAt(i)
    if num => zone.keyLo && num <= zone.keyHi && vel => zone.velLo && vel <= zone.velHi
      note = num + zone.transpose
      attackVel = curve(vel, zone.curve) * (zone.scale / 100) + zone.offset
      sendMidi(NOTE_ON, zone.channel, note, attackVel)
      
def noteOff(num, vel)
  for(i=0;i<sizeof(zones);i+1)
    zone = zones.getAt(i)
    if num => zone.keyLo && num <= zone.keyHi && attackVel[num] => zone.velLo && vel <= zone.velHi
      note = num + zone.transpose
      releaseVel = curve(vel, zone.curve) * (zone.scale / 100) + zone.offset
      sendMidi(NOTE_OFF, zone.channel, note, releaseVel)
      
def setAT(num, val)
  for(i=0;i<sizeof(zones);i+1)
    zone = zones.getAt(i)
    if num => zone.keyLo && num <= zone.keyHi
      if zone.atMode == OFF
        continue
      else
        atVal = curve(val, zone.atCurve)
        if zone.atMode == MONO
          sendMidi(MONO_AT, zone.channel, atVal, null)
        elif zone.atMode == POLY
          sendMidi(POLY_AT, zone.channel, num + zone.transpose, atVal)


