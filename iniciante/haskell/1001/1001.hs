soma :: Int -> Int -> Int
soma x y = x + y

main :: IO()
main = do
  a_entrada <- getLine
  b_entrada <- getLine

  let a = read a_entrada :: Int
  let b = read b_entrada :: Int
  putStrLn ("X = " ++ show (soma a b))
