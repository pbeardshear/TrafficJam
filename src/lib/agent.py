
class Agent:
  """
    Superclass that represents any agent that navigates the state space

    All implementing classes will provide a common interface for 
    movement in the state space, communication broadcasting, and communication
    reception.
    
  """
  def __init__(self, x, y, xVelocity = 0.0, yVelocity = 0.0):
    self.x = x
    self.y = y
    self.vx = xVelocity
    self.vy = yVelocity
    self.ax = 0.0
    self.ay = 0.0
  
  def getPosition(self):
    return { 'x': self.x, 'y': self.y }
  
  def move(self, pos):
    # Step an agent forward based on their current velocity, and apply acceleration values
    self.x += self.vx
    self.y += self.vy
    self.vx = max(self.vx + self.ax, 0)
    self.vy = max(self.vy + self.ay, 0)
    if self.vx is 0:
      self.ax = 0.0
    if self.vy is 0:
      self.ay = 0.0
  
  def accelerate(self, xAmount, yAmount):
    # Agents aren't allowed to move backwards, so they cannot decelerate while at zero velocity
    if (self.vx == 0 and self.vy == 0 and (xAmount < 0 or yAmount < 0)):
      return
    self.ax += xAmount
    self.ay += yAmount
    
  def broadcast(self, message):
    pass
  
  def receive(self, message):
    pass
  
