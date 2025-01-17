def doesValidArrayExist(derived: List[int]) -> bool:
        fin = 0
        for i in derived:
          fin ^= i
        return fin == 0

if __name__ == "__main__":
  print(doesValidArrayExist([1,1,0])
