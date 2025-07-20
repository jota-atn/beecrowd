soma :: Int -> Int -> Int
soma x y = x + y

main :: IO()
main = do 
  x <- readLn
  y <- readLn
  putStrLn ("SOMA = " ++ show (soma x y))
