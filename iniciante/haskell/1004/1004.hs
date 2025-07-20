prod :: Int -> Int -> Int
prod x y = x * y

main :: IO()
main = do 
  x <- readLn
  y <- readLn

  putStrLn ("PROD = " ++ show (prod x y))
