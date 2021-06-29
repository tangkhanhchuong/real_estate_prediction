const SYSTEM_URL = "http://localhost:5000"

//get all locations

const districtSelect = document.querySelector("#district")
const getLocations = async (e) => {
  const res = await fetch(`${SYSTEM_URL}/locations`)
  const data = await res.json()
  const locations = data.locations.filter((l, i) => i >= 9 && i <= 30)
  locations.forEach((l) => {
    const opt = new Option(l)
    opt.selected = true
    districtSelect.append(opt)
  })
}
window.addEventListener("load", getLocations)

//estimate real estate price

const reForm = document.querySelector("form")
const onSubmit = async (e) => {
  e.preventDefault()

  const dataBody = Object.values(e.target).map((e) => e.value)
  const decodedData = {
    area: dataBody[0],
    used_area: dataBody[1],
    bedrooms: dataBody[2],
    bathrooms: dataBody[3],
    furniture_status: dataBody[4],
    balcony: dataBody[5],
    garage: dataBody[6],
    private_pool: dataBody[7],
    sovereignty_type: dataBody[8],
    district: dataBody[9],
  }
  console.log(decodedData)

  const res = await axios.post(`${SYSTEM_URL}/predict`, {
    body: decodedData,
  })
  const data = await res.data

  const estimatedPrice = document.querySelector("#estimated_price")
  console.log(estimatedPrice, data)
  estimatedPrice.innerText = data.estimated_price
}
reForm.addEventListener("submit", onSubmit)

//control number input

const onNumberInputChange = (e) => {
  const target = e.target
  if (isNaN(target.value))
    target.value = target.value.slice(0, target.value.length - 1)

  if (target.value.length === 2 && target.value[0] == 0)
    target.value = target.value.slice(1, target.value.length)

  if (target.value.length === 0) target.value = 0
}

const inputs = document.querySelectorAll("input")
for (let input of inputs) {
  console.log(input)
  input.addEventListener("input", onNumberInputChange)
}
