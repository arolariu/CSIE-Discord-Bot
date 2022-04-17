import { Collection, Role } from "discord.js";

function filterByCareerPathRoles(role: Role): boolean {
  const filteredRoles = [
    "Data Scientist",
    "Software Developer",
    "Web Developer",
    "Graphics Industry",
    "Game Industry",
  ];
  return filteredRoles.includes(role.name);
}

function filterByUniversityRoles(role: Role): boolean {
  const filteredRoles = ["CIBERNETICĂ", "INFORMATICĂ ECONOMICĂ", "STATISTICĂ"];
  return filteredRoles.includes(role.name);
}

function filterByAdminRoles(role: Role): boolean {
  const filteredRoles = ["Admin", "Moderator", "Helper"];
  return filteredRoles.includes(role.name);
}

function filterByYearRoles(role: Role): boolean {
  const filteredRoles = ["AN I", "AN II", "AN III", "AN IV+"];
  return filteredRoles.includes(role.name);
}

function filterByTechRoles(role: Role): boolean {
  const filteredRoles = ["C/C++", "Python", "Java", "JavaScript", "C#"];
  return filteredRoles.includes(role.name);
}

function filterToUseByCategory(category: string): (role: Role) => boolean {
  switch (category) {
    case "Career Path":
      return filterByCareerPathRoles;
    case "University":
      return filterByUniversityRoles;
    case "Admin":
      return filterByAdminRoles;
    case "Year":
      return filterByYearRoles;
    case "Tech":
      return filterByTechRoles;
    default:
      throw new Error(`Unknown category to filter by: ${category}`);
  }
}

export default function filterRolesBasedOnCategory(
  roles: Collection<string, Role>,
  category: string
): Role[] {
  const filteredRoles: Role[] = [];
  const filterToUse: Function = filterToUseByCategory(category);

  roles.forEach((role) => {
    if (filterToUse(role)) {
      filteredRoles.push(role);
    }
  });

  return filteredRoles;
}
