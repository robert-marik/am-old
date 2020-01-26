{ decrease of water table in unconfined aquifer }
TITLE 'Snizeni rovinneho toku'     { the problem identification }

DEFINITIONS
k=1
s=50
T
sx1 = 0.5   sy1 = 0.5
srad = 0.1         
ngrid=1
source=0
l=1
polomer=0.01

VARIABLES        { system variables }
  h             { choose your own names }
 
  
EQUATIONS        { PDE's, one for each variable }
 h: div(T*grad(h))+source=0 { stationary 2D equation for underground flow in unconfined aquifer and datum level at h=0 }
 
 
INITIAL VALUES 
  h =10
  
BOUNDARIES       { The domain definition }
region 1
    T=k*(h)
    START(0,0)  natural(h)=0 LINE TO (1,0) 
    value(h)=20 line TO (1,1) 
    natural(h)=0 line TO (0,1) 
    value(h)=25 line TO CLOSE

    start(0.5,0.5-polomer)    value(h) = 15   arc(center=0.5,0.5) angle=-360 
 

MONITORS         { show progress }

PLOTS            { save result displays }
  CONTOUR(h)
  surface(h)
  vector (-grad(h)) points = (15,15)
END
