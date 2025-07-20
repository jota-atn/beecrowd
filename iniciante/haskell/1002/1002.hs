import Text.Printf (printf)

my_pi :: Double
my_pi = 3.14159

area :: Double -> Double
area x = my_pi * (x ** 2)

main :: IO ()
main = do
  x <- readLn
  printf "A=%.4f\n" (area x)

