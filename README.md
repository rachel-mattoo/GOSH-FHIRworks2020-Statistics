# GOSH-FHIRworks2020-Statistics
Display various patient statistics in a visual format

## Set-up 
Use [pip](https://pip.pypa.io/en/stable/) which is a python package installer to install all the required libraries used in the code. There are not too many and your IDE should let you install via the IDE itself. If not, use the following command:

```bash
  pip install
```

I used [FHIRworks_2020](https://github.com/greenfrogs/FHIRworks_2020) github repo to extract patient data. Carefully read the README instructions and ensure you have installed the correct versions for any required software and correctly setup the FHIR API credentials in appsettings.json. Now that you have the basics, clone this repository.

## Deploy

On the terminal, type
```powershell
cd FHIRworks_2020\dotnet-azure-fhir-web-api
```

Then run the following command in the terminal. This should work if everything has been set-up correctly. If not, refer back to the set-up instructions.

```powershell
dotnet run
```

As shown in the demo video, run api.py. You can either do this in visual studio or run the following command on the terminal:

```bash
python api.py
```

You can now choose which graph to display by running any of the following three commands:

```bash
python Graph1.py
python Graph2.py
python Graph_3.py
```


## Graph breakdown
**Graph 1 - Age Statistics** displays a horizontal bar chart of "average ages by gender"
<br />
**Graph 2 - Marriage Statistics** displays a stacked bar chart split by "proportion of married/unmarried females/males"
<br />
**Graph 3 - Language Statistics** dispays a chart of the number of patients who speak a particular language


## References 
[FHIR-parser](https://github.com/greenfrogs/FHIR-Parser) by Ethan Wood to simplify parsing patient data
<br />
[FHIRworks_2020](https://github.com/greenfrogs/FHIRworks_2020) which we were given by GOSH
